# Copyright 2022 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from deepview.validator.metrics.detectionutils import match_gt_dt, filter_dt, \
    nan_to_last_num
from deepview.validator.exceptions import ZeroUniqueLabelsException
from deepview.validator.metrics.core import Metrics
import numpy as np


class DetectionMetrics(Metrics):
    """
    This class provides methods to calculate:

        - precision.
                -> overall precision.

                -> mAP 0.5, 0.75, 0.5-0.95.
        - recall.
                -> overall recall.

                -> mAR 0.5, 0.75, 0.5-0.95.
        - accuracy.
                -> overall accuracy.

                -> mACC 0.5, 0.75, 0.5-0.95.

    Other calculations such as IoU, false positive ratios,
    precision vs recall data are also handled in this class.
    Unit-test for this class is defined under:
        test/test_metrics.py

    Parameters
    ----------
        detectiondatacollection: DetectionDataCollection
            This contains the number of ground truths in
            the dataset and tp, fp, and fn per class.

    Raises
    ------
        InvalidIoUException
            This will raise an exception if the calculated
            IoU is invalid. i.e. less than 0 or greater than 1.

        DivisionByZeroException
                This will raise an exception if a division of zero
                is encountered when calculating precision, recall, or accuracy.

        ZeroUniqueLabelsException
                This method will raise an exception if the number of unique
                labels captured is zero.

        ValueError
            This will raise the exception if the provided parameters
            in certain methods does not conform to the specified data type
            or the parameters are out of bounds. i.e. The thresholds provided
            are greater than 1 or less than 0.
    """

    def __init__(
        self,
        detectiondatacollection=None
    ):
        super(DetectionMetrics, self).__init__()
        self.detectiondatacollection = detectiondatacollection
    
    def compute_overall_metrics(
            self,
            total_tp,
            total_fn,
            total_class_fp,
            total_local_fp):
        """
        This method computes the overall precision, recall, and accuracy.

            - overall precision = sum tp /
                (sum tp + sum fp (localization + classification)).
            - overall recall = sum tp /
                (sum tp + sum fn + sum fp (localization)).
            - overall accuracy  = sum tp /
                (sum tp + sum fn + sum fp (localization + classification)).

        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_compute_overall_metrics

        Parameters
        ----------
            total_tp: int
                Total number of true positives in the dataset.

            total_fn: int
                Total number of false negatives in the dataset.

            total_class_fp: int
                Total number of classification false positives in the dataset.

            total_local_fp: int
                Total number of localization false positives in the dataset.

        Returns
        -------
            overall metrics: list
                This contains overall precision, overall recall,
                and overall accuracy.

        Raises
        ------
            DivisionByZeroException
                This method will raise an exception if a division of zero
                is encountered when calculating precision, recall, or accuracy.
        """

        if total_tp == 0:
            precision, recall, accuracy = 0., 0., 0.
            if total_class_fp + total_local_fp == 0:
                precision = np.nan
            if total_fn == 0:
                recall = np.nan
            if total_class_fp + total_local_fp + total_fn == 0:
                accuracy = np.nan
            return [precision, recall, accuracy]
        else:
            overall_precision = self.compute_precision(
                total_tp, total_class_fp + total_local_fp)
            overall_recall = self.compute_recall(
                total_tp, total_fn + total_class_fp)
            overall_accuracy = self.compute_accuracy(
                total_tp, total_class_fp + total_local_fp, total_fn)
            return [overall_precision, overall_recall, overall_accuracy]

    def compute_detection_metrics(self, score_threshold):
        """
        This method calculates the mean average precision,
        recall, and accuracy for the iou thresholds [0.5, 0.75, 0.5-0.95].

            - mean average precision = (sum of precision for every label) /
                                (total number of unique labels).
            - mean average recall = (sum of recall for every label) /
                                (total number of unique labels).
            - mean average accuracy = (sum of accuracy for every label) /
                                (total number of unique labels).

        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_compute_detection_metrics

        Parameters
        ----------
            score_threshold: float
                The score threshold to consider for predictions.

        Returns
        -------
            class metrics: list
                This contains mean average precision, recall, and accuracy
                at IoU threshold 0.5, 0.75, and 0.5-0.95

            class histogram data: dict
                This contains the number of true positives,
                false positives, and false negatives and
                aswell as precision, recall, and accuracy at
                IoU threshold 0.5 to plot as a histogram.

        Raises
        ------
            ZeroUniqueLabelsException
                This method will raise an exception if the number of unique
                labels captured is zero.

            DivisionByZeroException
                This method will raise an exception if a division of zero
                is encountered when calculating precision, recall, or accuracy.
        """

        score_threshold = self.validate_threshold(score_threshold)

        mmap, mar, macc = np.zeros(10), np.zeros(10), np.zeros(10)
        class_histogram_data = dict()
        non_zero = True

        num_class = len(self.detectiondatacollection.label_data_list)
        if num_class == 0:
            raise ZeroUniqueLabelsException()

        for label_data in self.detectiondatacollection.label_data_list:
            for it, iou_threshold in enumerate(np.arange(0.5, 1, 0.05)):

                tp = label_data.get_tp_count(iou_threshold, score_threshold)
                class_fp = label_data.get_class_fp_count(
                    iou_threshold, score_threshold)
                local_fp = label_data.get_local_fp_count(
                    iou_threshold, score_threshold)
                fn = label_data.get_fn_count(iou_threshold, score_threshold)

                precision, recall, accuracy = 0., 0., 0.
                if tp == 0:
                    precision, recall, accuracy = 0., 0., 0.
                    if non_zero:
                        if class_fp + local_fp == 0:
                            precision = np.nan
                        if fn == 0:
                            recall = np.nan
                        if class_fp + local_fp + fn == 0:
                            accuracy = np.nan
                        mmap[it] = precision
                        mar[it] = recall
                        macc[it] = accuracy
                else:
                    non_zero = False
                    precision = self.compute_precision(tp, class_fp + local_fp)
                    recall = self.compute_recall(tp, fn)
                    accuracy = self.compute_accuracy(
                        tp, class_fp + local_fp, fn)
                    
                    mmap = np.nan_to_num(mmap,nan=0)
                    mar = np.nan_to_num(mar,nan=0)
                    macc = np.nan_to_num(macc,nan=0)
      
                    mmap[it] += precision
                    mar[it] += recall
                    macc[it] += accuracy

                # Only consider IoU threshold at 0.5
                if it == 0:
                    class_histogram_data[str(label_data.get_label())] = {
                        'precision': precision,
                        'recall': recall,
                        'accuracy': accuracy,
                        'tp': int(label_data.get_tp_count(
                            0.50, score_threshold)),
                        'fn': int(label_data.get_fn_count(
                            0.50, score_threshold)),
                        'fp': int(label_data.get_class_fp_count(
                            0.50, score_threshold
                        ) + label_data.get_local_fp_count(
                            0.50, score_threshold
                        )),
                        'gt': int(label_data.gt)
                    }

        mmap /= num_class
        mar /= num_class
        macc /= num_class

        map_5095, mar_5095, macc_5095 = np.sum(
            mmap) / 10, np.sum(mar) / 10, np.sum(macc) / 10
        metric_map, metric_mar, metric_maccuracy = [
            mmap[0], mmap[5], map_5095], [
            mar[0], mar[5], mar_5095], [
            macc[0], macc[5], macc_5095]

        return [metric_map, metric_mar, metric_maccuracy], class_histogram_data

    def get_pr_data(
        self,
        score_threshold=0.5,
        iou_threshold=0.5,
        eps=1e-16,
        interval=0.01
        ):
        """
        This method computes the precision and recall
        based on varying score thresholds.
        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_get_pr_data

        Parameters
        ----------
            score_threshold: float
                The score threshold to consider for predictions.

            iou_threshold: float
                The IoU threshold to consider true positives.

            eps: float
                Minimum value to substitute for zero.

            interval: float
                Score threshold interval to test
                from eps (min)...1. + interval (max)

        Returns
        -------
            data for plots:
                precision, recall, names

        Raises
        ------
            ZeroUniqueLabelsException
                This method will raise an exception if the number of unique
                labels captured is zero.

            DivisionByZeroException
                This method will raise an exception if a division of zero
                is encountered when calculating precision and recall.
        """

        score_threshold = self.validate_threshold(score_threshold)
        iou_threshold = self.validate_threshold(iou_threshold)

        # All unique classes found at 0.01 detection threshold
        if len(self.detectiondatacollection.all_labels) == 0:
            if len(self.detectiondatacollection.labels) == 0:
                raise ZeroUniqueLabelsException()
            else:
                all_labels = self.detectiondatacollection.labels
                nc = len(all_labels)
        else:
            all_labels = self.detectiondatacollection.all_labels
            nc = len(all_labels)
        
        score_min, score_max = eps, 1. + interval
        score_thresholds = np.arange(score_min, score_max, interval)

        # Precision and recall, rows = classes, columns = range of thresholds
        p = np.zeros((nc, len(score_thresholds)))
        r = np.zeros((nc, len(score_thresholds)))
        # Average Precision, rows = classes, columns = range of IoUs (0.5-0.95)
        ap = np.zeros((nc, 10))
        
        # Iterate the range of thresholds
        for ti, score_t in enumerate(score_thresholds):
            # Reset the data
            self.detectiondatacollection.reset_containers()
            instances = self.detectiondatacollection.get_instances()

            for _, instance in instances.items():
                gt_boxes = instance.get('gt_instance').get('boxes')
                dt_boxes = instance.get('dt_instance').get('boxes')
                gt_labels = instance.get('gt_instance').get('labels')
                dt_labels = instance.get('dt_instance').get('labels')
                scores = instance.get('dt_instance').get('scores')

                # Filter detections only for valid scores based on threshold.
                dt_boxes, dt_labels, scores = filter_dt(
                    dt_boxes, dt_labels, scores, score_t)
                instance['dt_instance']['boxes'] = dt_boxes
                instance['dt_instance']['labels'] = dt_labels
                instance['dt_instance']['scores'] = scores

                # Match ground truths to detections
                self.detectiondatacollection.capture_class(dt_labels)
                self.detectiondatacollection.capture_class(gt_labels)
                stats = match_gt_dt(gt_boxes, dt_boxes)
                # Evaluate
                self.detectiondatacollection.categorize(
                    *stats,
                    gt_labels=gt_labels,
                    dt_labels=dt_labels,
                    scores=scores)
            
            # Precision for each class at this threshold.
            class_precision, class_recall = np.zeros(nc), np.zeros(nc)
           
            # Iterate through each data and grab precision and recall
            for label_data in self.detectiondatacollection.label_data_list:

                tp = label_data.get_tp_count(iou_threshold, score_t)
                class_fp = label_data.get_class_fp_count(
                    iou_threshold, score_t)
                local_fp = label_data.get_local_fp_count(
                    iou_threshold, score_t)
                fn = label_data.get_fn_count(iou_threshold, score_t)
               
                # Number of ground truth labels for this class
                n_l = label_data.get_gt()
                # Number of predictions for this class
                n_p = tp + class_fp + local_fp
                # The index to store the precision and recall based on class
                ci = all_labels.index(label_data.get_label())

                if n_p != 0 and n_l != 0:
                    if (tp + class_fp + local_fp) == 0:
                        # A division of 0/0 is not a number
                        class_precision[ci] = np.nan
                    else:
                        precision = self.compute_precision(
                            tp, class_fp + local_fp)
                        class_precision[ci] = precision

                    if (tp + fn) == 0:
                        # A division of 0/0 is not a number
                        class_recall[ci] = np.nan
                    else:
                        recall = self.compute_recall(tp, fn)
                        class_recall[ci] = recall
                else:
                    class_precision[ci] = np.nan
                    class_recall[ci] = np.nan

                if round(score_t, 2) == round(score_threshold, 2):
                    # AP from recall-precision curve
                    ap[ci, :] = self.compute_ap_iou(
                        label_data, score_threshold)
            
            p[:, ti] = class_precision
            r[:, ti] = class_recall

        # This portion replaces NaN values with the last acceptable values.
        # This is necessary so that the lengths are the same for both 
        # precision and recall. 
        for ci in range(nc):
            p[ci] = nan_to_last_num(p[ci])
            r[ci] = nan_to_last_num(r[ci])

        return {
            "precision": p,
            "recall": r,
            "average precision": ap,
            "names": all_labels
        }

    def get_plots_data(
            self,
            score_threshold=0.5,
            iou_threshold=0.5,
            eps=1e-16,
            interval=0.01
        ):
        """
        This method computes the precision and recall
        based on varying score thresholds to
        acquire data for the plots:

            - precision vs recall curve
            - precision vs confidence curve
            - recall vs confidence curve
            - f1 vs confidence curve

        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_get_pr_data

        Parameters
        ----------
            score_threshold: float
                The score threshold to consider for predictions.

            iou_threshold: float
                The IoU threshold to consider true positives.

            eps: float
                Minimum value to substitute for zero.

            interval: float
                Score threshold interval to test
                from eps (min)...1. + interval (max)

        Returns
        -------
            data for plots: dict

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

        Raises
        ------
            ZeroUniqueLabelsException
                This method will raise an exception if the number of unique
                labels captured is zero.

            DivisionByZeroException
                This method will raise an exception if a division of zero
                is encountered when calculating precision and recall.
        """

        iou_threshold = self.validate_threshold(iou_threshold)

        # number of unique classes
        all_labels = self.detectiondatacollection.all_labels
        nc = len(all_labels)
        if nc == 0:
            raise ZeroUniqueLabelsException()

        score_min, score_max = eps, 1. + interval
        score_thresholds = np.arange(score_min, score_max, interval)

        px = np.linspace(0, 1, 1000)
        overall_precision, overall_recall = list(), list()
        names, pred_scores = all_labels, list()
        ap, p, r = np.zeros(
            (nc, 10)), np.zeros(
            (nc, 1000)), np.zeros(
            (nc, 1000))
        
        self.detectiondatacollection.reset_containers()
        instances = self.detectiondatacollection.get_instances()

        # Rematch the unfiltered detections (low NMS score threshold) 
        for _, instance in instances.items():
            gt_boxes = instance.get('gt_instance').get('boxes')
            dt_boxes = instance.get('dt_instance').get('boxes')
            gt_labels = instance.get('gt_instance').get('labels')
            dt_labels = instance.get('dt_instance').get('labels')
            scores = instance.get('dt_instance').get('scores')

            # Match
            self.detectiondatacollection.capture_class(dt_labels)
            self.detectiondatacollection.capture_class(gt_labels)
            stats = match_gt_dt(gt_boxes, dt_boxes)
            # Evaluate
            self.detectiondatacollection.categorize(
                *stats,
                gt_labels=gt_labels,
                dt_labels=dt_labels,
                scores=scores)

        for label_data in self.detectiondatacollection.label_data_list:
            class_precision, class_recall = list(), list()
            ci = all_labels.index(label_data.get_label())
            # The number of ground truth labels for this class
            n_l = label_data.gt
            # The number of predictions for this class
            n_p = label_data.get_tp_count(iou_threshold, score_min) + \
                label_data.get_class_fp_count(iou_threshold, score_min) + \
                label_data.get_local_fp_count(iou_threshold, score_min)

            if n_p == 0 or n_l == 0:
                class_precision = np.zeros(int(score_max / interval))
                class_recall = np.zeros(int(score_max / interval))
                p[ci] = np.zeros(1000)
                r[ci] = np.zeros(1000)
            else:
                for score_t in score_thresholds:
                    tp = label_data.get_tp_count(iou_threshold, score_t)
                    class_fp = label_data.get_class_fp_count(
                        iou_threshold, score_t)
                    local_fp = label_data.get_local_fp_count(
                        iou_threshold, score_t)
                    fn = label_data.get_fn_count(iou_threshold, score_t)

                    if (tp + class_fp + local_fp) != 0:
                        precision = self.compute_precision(
                            tp, class_fp + local_fp)
                        class_precision.append(precision)
                    else:
                        # A division of 0/0 is not a number
                        class_precision.append(np.nan)

                    if (tp + fn) != 0:
                        recall = self.compute_recall(tp, fn)
                        class_recall.append(recall)
                    else:
                        # A division of 0/0 is not a number
                        class_recall.append(np.nan)

                # Find the maximum index where the value is not a NaN.
                precision_repeat_id = np.max(
                    np.argwhere(
                        np.logical_not(
                            np.isnan(class_precision))).flatten())
                recall_repeat_id = np.max(
                    np.argwhere(
                        np.logical_not(
                            np.isnan(class_recall))).flatten())
                # NaN values should be replace with the last acceptable value.
                class_precision = np.nan_to_num(
                    class_precision,
                    nan=class_precision[int(precision_repeat_id)]
                )
                class_recall = np.nan_to_num(
                    class_recall, nan=class_recall[int(recall_repeat_id)])

                # prediction scores
                tp_scores = label_data.get_tp_scores()
                class_fp_scores = label_data.get_class_fp_scores()
                local_fp_scores = label_data.get_local_fp_scores()
                pred_scores = np.concatenate(
                    (tp_scores, class_fp_scores, local_fp_scores), axis=None)
                i = np.argsort(-pred_scores)
                pred_scores = pred_scores[i]

                # Precision/Recall-Confidence curves
                recall_interp, precision_interp = list(), list()

                for score in pred_scores:
                    idx = (np.abs(score_thresholds - score)).argmin()
                    recall_interp = np.append(recall_interp, class_recall[idx])
                    precision_interp = np.append(
                        precision_interp, class_precision[idx])

                # negative x, xp because xp decreases
                r[ci] = np.interp(-px, -pred_scores, recall_interp, left=0)
                p[ci] = np.interp(-px, -pred_scores,
                                  precision_interp, left=1)  # p at pr_score

                class_precision = np.flip(class_precision)
                class_recall = np.flip(class_recall)

                # AP from recall-precision curve
                ap[ci, :] = self.compute_ap_iou(label_data, score_threshold)

            overall_precision.append(class_precision)
            overall_recall.append(class_recall)
            
        # Compute F1 (harmonic mean of precision and recall)
        f1 = 2 * p * r / (p + r + eps)

        return {
            "precision": overall_precision,
            "recall": overall_recall,
            "average-precision": ap,
            "x-data": px,
            "f1": f1,
            "precision-confidence": p,
            "recall-confidence": r,
            "names": names
        }

    def compute_ap_iou(self, label_data, score_threshold):
        """
        This method computes the precision for a specific class
        at 10 different iou thresholds.
        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_compute_ap_iou

        Parameters
        ----------
            label_data: DetectionLabelData
                A container for the number of tp, fp, and fn for the label.

            score_threshold: float
                The score threshold to consider for predictions.

        Returns
        -------
            precision: np.ndarray
                precision values for each IoU threshold (0.5-0.95).

        Raises
        ------
            ValueError
                This method will raise an exception if the
                provided score_threshold is not a floating point
                type and is out bounds meaning it is
                greater than 1 or less than 0.

            DivisionByZeroException
                This method will raise an exception if a division by
                zero occurs when calculating the precision.
        """

        score_threshold = self.validate_threshold(score_threshold)
        precision_list = np.zeros(10)
        for i, iou_threshold in enumerate(np.arange(0.5, 1, 0.05)):
            tp = label_data.get_tp_count(iou_threshold, score_threshold)
            class_fp = label_data.get_class_fp_count(
                iou_threshold, score_threshold)
            local_fp = label_data.get_local_fp_count(
                iou_threshold, score_threshold)
            if tp != 0:
                precision_list[i] = self.compute_precision(
                        tp, class_fp + local_fp)
        return precision_list

    def get_fp_error(self, score_threshold):
        """
        This method calculates the false positive error ratios.

        * Localization FP Error = Localization FP /
                            (Classification FP + Localization FP).
        * Classification FP Error = Classification FP /
                            (Classification FP + Localization FP).

        *Note: localization false positives are predictions
        that do no correlate to a ground truth. Classification
        false positives are predictions with non matching labels.*
        Unit-test for this method is defined under:
            file: test/deepview/validator/metrics/test_detectionmetrics.py
            function: test_get_fp_error

        Parameters
        ----------
            score_threshold: float
                The score threshold to consider for predictions.

        Returns
        -------
            Error Ratios: list
                This contains false positive ratios for
                IoU thresholds (0.5, 0.75, 0.5-0.95).

        Raises
        ------
            ValueError
                This method will raise an exception
                if the provided score_threshold is
                not a floating point type and is out
                bounds meaning it is
                greater than 1 or less than 0.

            DivisionByZeroException
                This method will raise an exception if a division by
                zero occurs when calculating the error ratios.
        """

        if not (isinstance(score_threshold, float)):
            raise ValueError(
                "The provided score_threshold does not have the correct " +
                "type. Can only accept floating type, but was provided " +
                "with score: {}".format(
                    type(score_threshold)))

        if (score_threshold < 0 or score_threshold > 1):
            raise ValueError(
                "The provided score_threshold is out of bounds: {}. ".format(
                    score_threshold) + 
                "Can only accept values between 0 and 1.")
        else:
            local_fp_error, class_fp_error = np.zeros(10), np.zeros(10)
            for it, iou_threshold in enumerate(np.arange(0.5, 1, 0.05)):
                _, _, \
                    class_fp, local_fp = \
                        self.detectiondatacollection.sum_outcomes(
                        iou_threshold, score_threshold
                    )
                if local_fp == 0:
                    local_fp_error[it] = 0
                else:
                    local_fp_error[it] = self.divisor(
                        local_fp, local_fp + class_fp)
                if class_fp == 0:
                    class_fp_error[it] = 0
                else:
                    class_fp_error[it] = self.divisor(
                        class_fp, local_fp + class_fp)
            return [local_fp_error[0], class_fp_error[0],
                    local_fp_error[5], class_fp_error[5],
                    np.sum(local_fp_error) / 10, np.sum(class_fp_error) / 10]
