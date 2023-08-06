# Copyright 2022 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from deepview.validator.metrics import DetectionMetrics, \
    DetectionDataCollection
from deepview.validator.metrics.detectionutils import match_gt_dt, filter_dt, \
    clamp_boxes, ignore_boxes
from deepview.validator.visualize.utils import plot_pr, plot_classification, \
    figure2numpy, close_figures
from deepview.validator.visualize import DetectionDrawer
from deepview.validator.evaluators.core import Evaluator
from deepview.validator.writers.core import Writer
from copy import deepcopy
from os import path
import numpy as np


class DetectionEval(Evaluator):
    """
    This class provides methods to perform detection validation.
    The common process of running validation:

        1) Grab the ground truth and the model prediction instances per image.
        2) Match the  model predictions to the ground truth.
        3) Categorize the model predictions as either true positives,
           or false positives/negatives.
        4) Draw the bounding boxes.
        5) Calculate the metrics.

    Unit-test for this class is defined under:
        file: test/deepview/validator/evaluators/test_detectionevaluator.py

    Parameters
    ----------
        runner: Runner object depending on the model.
            This object provides methods to run the detection model.

        dataset: Dataset object depending on the dataset.
            This object provides methods to read and parse the dataset.

        visualize: str
            This is the path to store the images with visualizations. Can
            optionally be None to exclude.

        tensorboard: str
            This is the path to store the tensorboard tfevents file. Can
            optionally be None to exclude.

        json_out: str
            This is the path to the store the JSON file validation
            summary.

        display: int
            This is the number of images to save. By default it is -1
            specifying all the images.

        parameters: dict
            The model parameters:

            .. code-block:: python

                {
                    "validation-iou": args.validation_iou,
                    "detection-iou": args.detection_iou,
                    "validation-threshold": args.validation_threshold,
                    "detection-threshold": args.detection_threshold,
                    "nms": args.nms_type,
                    "normalization": args.norm,
                    "maximum_detections": args.max_detection,
                    "warmup": args.warmup
                }

    Raises
    -------
        ValueError
            This will raise the exception if the provided parameters
            in certain methods does not conform to the specified data type
            or the parameters are out of bounds. i.e. The thresholds provided
            are greater than 1 or less than 0.

    """

    def __init__(
        self,
        runner=None,
        dataset=None,
        visualize=None,
        tensorboard=None,
        json_out=None,
        display=-1,
        parameters=None,
        full_summary=False
    ):
        super(DetectionEval, self).__init__(
            runner=runner,
            dataset=dataset,
            datacollection=DetectionDataCollection(),
            visualize=visualize,
            tensorboard=tensorboard,
            json_out=json_out,
            display=display,
            parameters=parameters
        )

        self.drawer = DetectionDrawer()
        self.clamp_box = self.parameters.get("clamp boxes")
        self.ignore_box = self.parameters.get("ignore boxes")
        self.full_summary = full_summary

    def __call__(self, val_messenger):
        """
        This method allows tensorboardformatter object in trainer
        to operate here and resets the metrics after each epoch.
        Default validation has no use of this method.
        Unit-test for this method is defined under:
            file: test/deepview/validator/evaluators/test_detectionevaluator.py
            function: test__call__.py

        Parameters
        ----------
            val_messenger: TrainingTensorBoardWriter
                This object is internal for modelpack that was instantiated
                specifically for training a model.

        Returns
        -------
            None

        Raises
        ------
            None
        """

        self.tensorboardwriter = val_messenger
        self.datacollection = DetectionDataCollection()

    def instance_collector(self):
        """
        This method collects the instances from the ground truth
        and the model predictions.
        Unit-test for this method is defined under:
            file: test/deepview/validator/evaluators/test_detectionevaluator.py
            function: test_instance_collector

        Parameters
        ----------
            None

        Returns
        -------
            instances: dict
                This yields one image instance from the ground
                truth and the model predictions.
                See README.md (Method Parameters Format) for more information.

        Raises
        ------
            ValueError
                This method will raise an exception if provided image path
                does not exist and the provided image array
                is not a numpy.ndarray.
        """

        for gt_instance in self.dataset.read_all_samples():
            # This is for gray images that can't be processed.
            if gt_instance is None:
                continue

            if path.exists(gt_instance.get('image_path')):
                image = gt_instance.get('image_path')
            elif isinstance(gt_instance.get('image'), np.ndarray):
                image = gt_instance.get('image')
            else:
                raise ValueError(
                    "The provided image_path does not exist at: " +
                    gt_instance.get('image_path') +
                    "The provided image array is not a numpy.ndarray: " +
                    type(gt_instance.get('image'))
                )

            output = self.runner.run_single_instance(image)
            if output is not None:
                dt_boxes, dt_classes, dt_scores = output
            else:
                yield {
                'gt_instance': None,
                'dt_instance': None
            }
            
            # Convert any synonym of the predicted label into the standard coco
            # label.
            if "clock" in self.dataset.labels:
                dt_classes_modified = list()
                for label in dt_classes:
                    for key in self.runner.sync_dict.keys():
                        if label == key:
                            label = self.runner.sync_dict[key]
                    dt_classes_modified.append(label)
                dt_classes = dt_classes_modified

            dt_instance = {
                'boxes': dt_boxes,
                'labels': dt_classes,
                'scores': dt_scores
            }

            yield {
                'gt_instance': gt_instance,
                'dt_instance': dt_instance
            }

    def single_evaluation(self, instance, epoch=0, add_image=False):
        """
        This method runs validation on a single instance.
        Unit-test for this method is defined under:
            file: test/deepview/validator/evaluators/test_detectionevaluator.py
            function: test_single_evaluation

        Parameters
        ----------
            instance: dict
                The ground truth and the predictions instances.
                See README.md (Method Parameters Format) for more information.

            epoch: int
                This is the training epoch number. This
                parameter is internal for modelpack usage.
                Default validation has no use of this parameter.

            add_image: bool
                If set to True, this will draw on the image
                with bounding boxes.

        Returns
        -------
            truth values: int
                total_tp, total_fn, total_class_fp, total_local_fp

        Raises
        ------
            ValueError
                This will raise the exception if the provided parameters
                in certain methods does not conform to the specified data
                type or the parameters are out of bounds. i.e.
                The thresholds provided
                are greater than 1 or less than 0.
        """

        iou_t = self.parameters.get("validation-iou")
        score_t= self.parameters.get("validation-threshold")
        gt_instance = instance.get("gt_instance")
        dt_instance = instance.get("dt_instance")

        # Store all unfiltered detections. 
        key = path.basename(gt_instance.get('image_path'))
        original_instance = {
            'gt_instance': {
                "height": gt_instance.get("height"),
                "width": gt_instance.get("width"),
                "boxes": gt_instance.get("boxes"),
                "labels": gt_instance.get("labels")
            },
            'dt_instance': {
                "boxes": dt_instance.get("boxes"),
                "labels": dt_instance.get("labels"),
                "scores": dt_instance.get("scores")
            }
        }
        self.datacollection.capture_all_class(
            original_instance.get("gt_instance").get("labels"))
        self.datacollection.capture_all_class(
            original_instance.get("dt_instance").get("labels"))
        self.datacollection.append_instance(key, original_instance)

        # Filter detections only for valid scores.
        dt_boxes, dt_labels, scores = filter_dt(
            dt_instance.get("boxes"), 
            dt_instance.get("labels"), 
            dt_instance.get("scores"), 
            score_t)
        instance['dt_instance']['boxes'] = dt_boxes
        instance['dt_instance']['labels'] = dt_labels
        instance['dt_instance']['scores'] = scores

        if self.clamp_box:
            instance = clamp_boxes(instance, self.clamp_box)
        if self.ignore_box:
            instance = ignore_boxes(instance, self.ignore_box)

        self.datacollection.capture_class(dt_instance.get("labels"))
        self.datacollection.capture_class(gt_instance.get("labels"))
        stats = match_gt_dt(
            gt_instance.get("boxes"), 
            dt_instance.get("boxes"), 
            self.parameters.get("metric"))
        self.datacollection.categorize(
            *stats,
            gt_labels=gt_instance.get("labels"),
            dt_labels=dt_instance.get("labels"),
            scores=dt_instance.get("scores"))

        if add_image:
            if self.visualize or self.tensorboardwriter:
                original_image = instance.get('gt_instance').get('image')
                image = self.drawer.draw_with_pillow(
                    iou_t, score_t,
                    original_image, instance, *stats
                )

            if self.visualize:
                image.save(path.join(self.save_path, path.basename(
                    instance.get('gt_instance').get('image_path'))))
            elif self.tensorboardwriter:
                nimage = np.asarray(image)
                self.tensorboardwriter(nimage, instance.get(
                    'gt_instance').get('image_path'), step=epoch)
        return self.datacollection.sum_outcomes(iou_t, score_t)

    def group_evaluation(self):
        """
        This method performs the bounding box evaluation on all images.
        Unit-test for this method is defined under:
            file: test/deepview/validator/evaluators/test_detectionevaluator.py
            function: test_group_evaluation

        Parameters
        ----------
            None

        Returns
        -------
            truth values: int
                total_tp, total_fn, total_class_fp, total_local_fp

        Raises
        ------
            ValueError
                This will raise the exception if the provided parameters
                in certain methods does not conform to the specified data type
                or the parameters are out of bounds.
                i.e. The thresholds provided
                are greater than 1 or less than 0.
        """

        iou_threshold = self.parameters.get("validation-iou")
        score_threshold = self.parameters.get("validation-threshold")
        self.counter = 0

        for instances in self.instance_collector():

            gt_instance = instances.get("gt_instance")
            dt_instance = instances.get("dt_instance")

            if None in [gt_instance, dt_instance]:
                Writer.logger(
                    "VisionPack Trial Expired. Please use a licensed version" + 
                    " for complete validation. Contact support@au-zone.com" +
                    " for more information.", code="WARNING")
                break

            # Store all unfiltered detections. 
            key = path.basename(gt_instance.get('image_path'))
            original_instance = {
                'gt_instance': {
                    "height": gt_instance.get("height"),
                    "width": gt_instance.get("width"),
                    "boxes": gt_instance.get("boxes"),
                    "labels": gt_instance.get("labels")
                },
                'dt_instance': {
                    "boxes": dt_instance.get("boxes"),
                    "labels": dt_instance.get("labels"),
                    "scores": dt_instance.get("scores")
                }
            }
            self.datacollection.capture_all_class(
                original_instance.get("gt_instance").get("labels"))
            self.datacollection.capture_all_class(
                original_instance.get("dt_instance").get("labels"))
            self.datacollection.append_instance(key, original_instance)
            
            # Filter detections only for valid scores.
            dt_boxes, dt_labels, scores = filter_dt(
                dt_instance.get("boxes"), 
                dt_instance.get("labels"), 
                dt_instance.get("scores"), 
                score_threshold)
            instances['dt_instance']['boxes'] = dt_boxes
            instances['dt_instance']['labels'] = dt_labels
            instances['dt_instance']['scores'] = scores

            if self.clamp_box:
                instances = clamp_boxes(instances, self.clamp_box)
            if self.ignore_box:
                instances = ignore_boxes(instances, self.ignore_box)

            self.datacollection.capture_class(dt_instance.get("labels"))
            self.datacollection.capture_class(gt_instance.get("labels"))
            stats = match_gt_dt(
                gt_instance.get("boxes"), 
                dt_instance.get("boxes"), 
                self.parameters.get("metric"))
            self.datacollection.categorize(
                *stats,
                gt_labels=gt_instance.get("labels"),
                dt_labels=dt_instance.get("labels"),
                scores=dt_instance.get("scores"))

            if self.visualize or self.tensorboardwriter:
                original_image = instances.get('gt_instance').get('image')
                image = self.drawer.draw_with_pillow(
                    iou_threshold, score_threshold,
                    original_image, instances, *stats)

                if self.display >= 0:
                    if self.counter < self.display:
                        self.counter += 1
                    else:
                        continue

            if self.visualize:
                image.save(path.join(self.save_path, path.basename(
                    instances.get('gt_instance').get('image_path'))))
            elif self.tensorboardwriter:
                nimage = np.asarray(image)
                self.tensorboardwriter(nimage, instances.get(
                    'gt_instance').get('image_path'))
            else:
                continue
        return self.datacollection.sum_outcomes(iou_threshold, score_threshold)

    def conclude(self, truth_values, epoch=0):
        """
        This method computes the final metrics, draws the final plots, and
        saves the results either to tensorboard or to the local machine.
        Unit-test for this method is defined under:
            file: test/deepview/validator/evaluators/test_detectionevaluator.py
            function: test_conclude

        Parameters
        ----------
            truth values: list
                total_tp, total_fn, total_class_fp, total_local_fp

            epoch: int
                This is the training epoch number. This
                parameter is internal for modelpack usage.
                Default validation has no use of this parameter.

        Returns
        -------
            summary: dict
                The validation summary.
                See README.md (Method Parameters Format) for more information.
                
        Raises
        ------
            None
        """
        
        metrics = DetectionMetrics(self.datacollection)
        if self.runner is not None:
            timings = self.runner.summarize()
            self.parameters["engine"] = self.runner.device
            self.parameters["maximum_detections"] = self.runner.max_detections
            self.parameters["nms"] = self.runner.nms_type
        else:
            timings = None

        # Grab the validation metrics
        overall_metrics = metrics.compute_overall_metrics(*truth_values)
        truth_values.append(self.datacollection.total_gt)
        mean_metrics, class_histogram_data = metrics.compute_detection_metrics(
            self.parameters.get("validation-threshold"))
        false_positive_ratios = metrics.get_fp_error(
            self.parameters.get("validation-threshold"))
        precision_recall_data = metrics.get_pr_data(
            self.parameters.get("validation-threshold"), 
            self.parameters.get("validation-iou")
        )
        
        # Contain the metrics inside a dictionary
        summary = self.create_summary(
            truth_values=truth_values,
            overall_metrics=overall_metrics,
            mean_metrics=mean_metrics,
            false_positive_ratios=false_positive_ratios,
            timings=timings)

        # Get, save, or publish plots
        if self.visualize or self.tensorboardwriter:
            plots = self.get_plots(
                summary.get("model"), 
                class_histogram_data, 
                precision_recall_data)
            
        if self.visualize:
            self.save_plots_disk(plots)
        elif self.tensorboardwriter:
            self.publish_plots(plots, summary.get("model"), epoch)

        if self.full_summary or self.json_out:
            summary["class_histogram_data"] = class_histogram_data
            summary["precision_recall_data"] = precision_recall_data
            if self.json_out:
                self.save_jsonsummary(summary)
            
        if self.tensorboardwriter:
            self.publish_metrics(summary, epoch)
        else:
            header, format_summary, format_timings = self.consolewriter(
                message=deepcopy(summary),
                parameters=self.parameters,
                validation_type="detection")
            
            if self.visualize:
                self.save_metrics_disk(header, format_summary, format_timings)    
        return summary
    
    def create_summary(
            self, 
            truth_values, 
            overall_metrics, 
            mean_metrics, 
            false_positive_ratios, 
            timings
        ):
        """
        This method creates a summary dictionary containing all the collected
        validation metrics.

        Parameters
        ----------
            truth_values: list
                total_tp, total_fn, total_class_fp, total_local_fp, total_gt
            
            overall_metrics: list
                This contains overall precision, overall recall,
                    and overall accuracy.

            mean_metrics: list
                This contains mean average precision, recall, and accuracy
                at IoU threshold 0.5, 0.75, and 0.5-0.95

            false_positive_ratio: list
                This contains false positive ratios for
                IoU thresholds (0.5, 0.75, 0.5-0.95).

            timings: dict

            .. code-block:: python

                {
                 'min_inference_time': minimum time to produce bounding boxes,
                 'max_inference_time': maximum time to produce bounding boxes,
                 'min_input_time': minimum time to load an image,
                 'max_input_time': maximum time to load an image,
                 'min_decoding_time': minimum time to process model
                                    predictions,
                 'max_decoding_time': maximum time to process model
                                    predictions,
                 'avg_decoding': average time to process model predictions,
                 'avg_input': average time to load an image,
                 'avg_inference': average time to produce bounding boxes,
                }

        Returns
        -------
            summary: dict
                The validation summary.
                See README.md (Method Parameters Format) for more information.

        Raises
        ------
            None
            
        """

        try:
            model_name = path.basename(path.normpath(self.runner.source))
        except AttributeError:
            model_name = "Training Model"

        try:
            dataset_name = path.basename(path.normpath(self.dataset.source))
        except AttributeError:
            dataset_name = "Validation Dataset"

        summary = {
            "model": model_name,
            "dataset": dataset_name,
            "numgt": truth_values[-1],
            "Total TP": truth_values[0],
            "Total FN": truth_values[1],
            "Total Class FP": truth_values[2],
            "Total Loc FP": truth_values[3],
            "OP": overall_metrics[0],
            "mAP": {'0.5': mean_metrics[0][0],
                    '0.75': mean_metrics[0][1],
                    '0.5:0.95': mean_metrics[0][2]
                    },
            "OR": overall_metrics[1],
            "mAR": {'0.5': mean_metrics[1][0],
                    '0.75': mean_metrics[1][1],
                    '0.5:0.95': mean_metrics[1][2]
                    },
            "OA": overall_metrics[2],
            "mACC": {'0.5': mean_metrics[2][0],
                     '0.75': mean_metrics[2][1],
                     '0.5:0.95': mean_metrics[2][2]
                     },
            "LocFPErr": {'0.5': false_positive_ratios[0],
                         '0.75': false_positive_ratios[2],
                         '0.5:0.95': false_positive_ratios[4]
                         },
            "ClassFPErr": {'0.5': false_positive_ratios[1],
                           '0.75': false_positive_ratios[3],
                           '0.5:0.95': false_positive_ratios[5]
                           },
            "timings": timings
        }
        return summary
    
    @staticmethod
    def get_plots(model_name, class_histogram_data, precision_recall_data):
        """
        This method gets the validation plots based on the data recieved.

        Parameters
        ----------
            model_name: str
                The name of the model being validated.

            class_histogram_data: dict
                This contains the number of true positives,
                false positives, and false negatives and
                aswell as precision, recall, and accuracy at
                IoU threshold 0.5 to plot as a histogram.

            precision_recall_data: dict
                .. code-block:: python

                    {
                        "precision"
                        "recall"
                        "average-precision"
                        "x-data"
                        "f1"
                        "precision-confidence"
                        "recall-confidence"
                        "names"
                    }

        Returns
        -------
            plots: list 
                This contains [fig_class_metrics, fig_prec_rec_curve, 
                fig_f1_curve, fig_prec_confidence_curve, 
                fig_rec_confidence_curve]

        Raises
        ------
            None
        """

        fig_class_metrics = plot_classification(
            class_histogram_data, model=model_name)
        fig_prec_rec_curve = plot_pr(
            precision_recall_data.get("precision"),
            precision_recall_data.get("recall"),
            precision_recall_data.get("average precision"),
            precision_recall_data.get("names"))
        return [fig_class_metrics, fig_prec_rec_curve]

    def save_plots_disk(self, plots):
        """
        This method saves the plots locally on disk.

        Parameters
        ----------
            plots: list
                [fig_class_metrics, fig_prec_rec_curve, fig_f1_curve, 
                fig_prec_confidence_curve, fig_rec_confidence_curve]

        Returns
        -------
            None

        Raises
        ------
            None
        """

        plots[0].savefig(
            f'{self.save_path}/class_scores.png',
            bbox_inches="tight")
        plots[1].savefig(
            f'{self.save_path}/prec_rec_curve.png',
            bbox_inches='tight')
        close_figures(plots)

    def publish_plots(self, plots, model_name="Training Model", epoch=0):
        """
        This method publishes the plots onto tensorboard.

        Parameters
        ----------
            plots: list
                [fig_class_metrics, fig_prec_rec_curve, fig_f1_curve, 
                    fig_prec_confidence_curve, fig_rec_confidence_curve]

            model_name: str
                The name of the model being validated.

            epoch: int
                The epoch number if it is a training model. 

        Returns
        -------
            None

        Raises
        ------
            None
        """

        nimage_class = figure2numpy(plots[0])
        nimage_precision_recall = figure2numpy(plots[1])

        self.tensorboardwriter(
            nimage_class,
            f"{model_name}_scores.png",
            step=epoch)
        self.tensorboardwriter(
            nimage_precision_recall,
            f"{model_name}_precision_recall.png",
            step=epoch)
        close_figures(plots)

    def save_metrics_disk(self, header, format_summary, format_timings):
        """
        This method saves the validation metrics onto a text file.

        Parameters
        ----------
            header: str
                The title of the validation metrics.

            format_summary: str
                The formatted validation showing the metrics.

            format_timings: str
                The formatted timings summary.

        Returns
        -------
            None

        Raises
        ------
            None
        """

        with open(self.save_path + '/metrics.txt', 'w') as fp:
            fp.write(header + '\n')
            fp.write(format_summary + '\n')
            if format_timings is not None:
                fp.write(format_timings)
            fp.close()

    def publish_metrics(self, summary, epoch=0):
        """
        This method publishes the metrics onto tensorboard.

        Parameters
        ----------
            summary: dict
                The validation summary.
                See README.md (Method Parameters Format) for more information.

            epoch: int
                The epoch number when training a model.

        Returns
        -------
            None

        Raises
        ------
            None 
        """
        self.tensorboardwriter.publish_metrics(
            message=deepcopy(summary),
            parameters=self.parameters,
            step=epoch,
            validation_type="detection")

    def save_jsonsummary(self, summary):
        """
        This method saves the summary dictionary as a JSON file.

        Parameters
        ----------
            summary: dict
                The validation summary.
                See README.md (Method Parameters Format) for more information.
        
        Returns
        -------
            None

        Raises
        ------
            None
        """
        import json
        reformat_pr_data = dict()
        for key, value in summary["precision_recall_data"].items():
            if isinstance(value, (list, np.ndarray)):
                tmp_value = list()
                for x in value:
                    if isinstance(x, np.ndarray):
                        tmp_value.append(x.tolist())
                    else:
                        tmp_value.append(x)
            elif isinstance(value, (np.int32)):
                tmp_value = int(value)
            else:
                pass
            reformat_pr_data[key] = tmp_value
        summary["precision_recall_data"] = reformat_pr_data
        # This is for debugging purposes...
        # self.print_types(summary)
        with open(self.json_out, 'w', encoding='utf-8') as fp:
            json.dump(summary, fp, ensure_ascii=False, indent=4)
            fp.close()