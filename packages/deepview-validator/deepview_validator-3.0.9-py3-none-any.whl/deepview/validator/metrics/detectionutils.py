# Copyright 2022 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from deepview.validator.exceptions import MatchingAlgorithmException
from deepview.validator.exceptions import InvalidIoUException
import numpy as np


def center_point_distance(boxA, boxB):
    """
    This method finds the distance between the center of two 
    bounding boxes using pythagoras. 

    Parameters
    ----------
        boxA: list or np.ndarray
            This contains [xmin, ymin, xmax, ymax] for detections.

        boxB: list or np.ndarray
            This contains [xmin, ymin, xmax, ymax] for ground truth.

    Returns
    -------
        center point distance: float
            This is the distance from center to center of the
            bounding boxes.

    Raises
    ------
        None
    """

    width_a = boxA[2] - boxA[0]
    width_b = boxB[2] - boxB[0]
    height_a = boxA[3] - boxA[1]
    height_b = boxB[3] - boxB[1]

    a = abs((boxA[0] + width_a/2) - (boxB[0] + width_b/2))
    b = abs((boxA[1] + height_a/2) - (boxB[1] + height_b/2))
    return (a**2 + b**2)**0.5

def bb_intersection_over_union(boxA, boxB, eps=1e-10):
    """
    This method computes the IoU between ground truth and detection
    bounding boxes.
    IoU computation method retrieved from:
    https://gist.github.com/meyerjo/dd3533edc97c81258898f60d8978eddc

    Parameters
    ----------
        boxA: list
            This is a bounding box [xmin, ymin, xmax, ymax]
        
        boxB: list
            This is a bounding box [xmin, ymin, xmax, ymax]

    Returns
    -------
        IoU: float
            The IoU score between boxes.

    Exceptions
    ----------
        InvalidIoUException
            This method will raise an exception if the calculated
            IoU is invalid. i.e. less than 0 or greater than 1.

        ValueError
            This method will raise an exception if the provided boxes for
            ground truth and detection does not have a length of four.
    """

    if len(boxA) != 4 or len(boxB) != 4:
        raise ValueError("The provided bounding boxes does not meet " \
                            "expected lengths [xmin, ymin, xmax, ymax]")
    
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max((xB - xA, 0)) * max((yB - yA), 0)
    if interArea == 0:
        return 0.
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs((boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    boxBArea = abs((boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    if iou > 1. + eps or iou < 0.:
        raise InvalidIoUException(iou)
    # return the intersection over union value
    return iou   

def bbox_iou(bboxes1, bboxes2, eps=1e-10):
    """
    This method computes the intersection over union.
    Unit-test for this method is defined under:
        file: test/deepview/validator/metrics/test_detectionmetrics.py
        function: test_bbox_iou

    Parameters
    ----------
        bboxes1: np.ndarray
            (a, b, ..., 4)

        bboxes2: np.ndarray
            (A, B, ..., 4)
            x:X is 1:n or n:n or n:1

        eps: float
            Invalid IoU leniency.

    Returns
    -------
        IoU score: float
            (max(a,A), max(b,B), ...)
            ex) (4,):(3,4) -> (3,)
                (2,1,4):(2,3,4) -> (2,3)

    Raises
    ------
        InvalidIoUException
            This method will raise an exception if the calculated
            IoU is invalid. i.e. less than 0 or greater than 1.

        ValueError
            This method will raise an exception if the provided boxes for
            ground truth and detection does not have a length of four.
    """

    if len(bboxes1) != 4 or len(bboxes2) != 4:
        raise ValueError("The provided bounding boxes does not meet " \
                            "expected lengths [xmin, ymin, xmax, ymax]")

    bboxes1_area = bboxes1[..., 2] * bboxes1[..., 3]
    bboxes2_area = bboxes2[..., 2] * bboxes2[..., 3]

    bboxes1_coor = np.concatenate(
        [
            bboxes1[..., :2] - bboxes1[..., 2:] * 0.5,
            bboxes1[..., :2] + bboxes1[..., 2:] * 0.5,
        ],
        axis=-1,
    )
    bboxes2_coor = np.concatenate(
        [
            bboxes2[..., :2] - bboxes2[..., 2:] * 0.5,
            bboxes2[..., :2] + bboxes2[..., 2:] * 0.5,
        ],
        axis=-1,
    )

    left_up = np.maximum(bboxes1_coor[..., :2], bboxes2_coor[..., :2])
    right_down = np.minimum(bboxes1_coor[..., 2:], bboxes2_coor[..., 2:])
    inter_section = np.maximum(right_down - left_up, 0.0)
    inter_area = inter_section[..., 0] * inter_section[..., 1]
    union_area = bboxes1_area + bboxes2_area - inter_area
    iou = inter_area / union_area

    if iou > 1. + eps or iou < 0.:
        raise InvalidIoUException(iou)
    return iou

def compute_iou(dt_box, gt_box, width=1, height=1, eps=1e-10):
    """
    This method computes the intersection over union.
    This computation was taken from the following source:
    https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/

    Unit-test for this method is defined under:
        file: test/deepview/validator/metrics/test_detectionmetrics.py
        function: test_compute_iou

    Parameters
    ----------
        dt_box: list or np.ndarray
            Model prediction box containing [x1, y1, x2, y2].

        gt_box: list or np.ndarray
            Ground truth box containing [x1, y1, x2, y2].

        width: int
            Width of the image to denormalize x coordinates.

        height: int
            Height of the image to denormalize y coordinates.

        eps: float
            Invalid IoU leniency.

    Returns
    -------
        IoU score: float
            The intersection over union between the prediction and the
            ground truth bounding box.

    Raises
    ------
        InvalidIoUException
            This method will raise an exception if the calculated
            IoU is invalid. i.e. less than 0 or greater than 1.

        ValueError
            This method will raise an exception if the provided boxes for
            ground truth and detection does not have a length of four.
    """

    if len(dt_box) != 4 or len(gt_box) != 4:
        raise ValueError("The provided bounding boxes does not meet " \
                            "expected lengths [xmin, ymin, xmax, ymax]")

    xa = max(float(gt_box[0]) * width, float(dt_box[0]) * width)
    ya = max(float(gt_box[1]) * height, float(dt_box[1]) * height)
    xb = min(float(gt_box[2]) * width, float(dt_box[2]) * width)
    yb = min(float(gt_box[3]) * height, float(dt_box[3]) * height)

    inter_area = max(0, xb - xa + 1) * max(0, yb - ya + 1)
    boxa_area = (float(dt_box[2]) * width - float(dt_box[0]) * width + 1)*(
        float(dt_box[3]) * height - float(dt_box[1]) * height + 1)
    boxb_area = (float(gt_box[2]) * width - float(gt_box[0]) * width + 1)*(
        float(gt_box[3]) * height - float(gt_box[1]) * height + 1)

    iou = inter_area / float(boxa_area + boxb_area - inter_area)

    if iou > 1. + eps or iou < 0.:
        raise InvalidIoUException(iou)
    return iou

def filter_dt(boxes, classes, scores, threshold):
    """
    This function filters the detections to include only scores 
    greater than or equal to the validation threshold set.
    

    Parameters
    ----------
        boxes: np.ndarray
            The prediction bounding boxes.. [[box1], [box2], ...]

        classes: np.ndarray
            The prediction labels.. [cl1, cl2, ...]

        scores: np.ndarray
            The prediction confidence scores.. [score, score, ...]
            normalized between 0 and 1.

        threshold: float
            This is the validation score threshold to filter
            the detections.

    Returns
    ------- 
        boxes, classes, scores: np.ndarray
            These contain only the detections whose scores are 
            larger than or greater than the validation threshold set.

    Raises
    ------
        None

    """
    filter_indices = np.argwhere(scores >= threshold).flatten()
    boxes = np.take(boxes, filter_indices, axis=0)
    scores = np.take(scores, filter_indices, axis=0)
    classes = np.take(classes, filter_indices, axis=0)
    return boxes, classes, scores

def clamp_boxes(instances, clamp):
    """
    This function clamps bounding box less than the provided clamp value to
    the clamp value in pixels. The minimum width and height of the bounding
    is the clamp value in pixels. 

    Parameters
    ----------
        instances: dict
            This contains the ground truth and the detection data.
            See README.md (Method Parameters Format) for more information.

        clamp: int
            The minimum acceptable dimensions of the bounding boxes for 
            detections and ground truth. 

    Returns
    -------
        instances: dict
            This now contains the updated clamped bounding boxes.

    Raises
    ------ 
        None
    """
    height = instances.get('gt_instance').get('height')
    width = instances.get('gt_instance').get('width')
    gt_boxes = instances.get('gt_instance').get('boxes')
    dt_boxes = instances.get('dt_instance').get('boxes')

    gt_widths = ((gt_boxes[..., 2:3] - gt_boxes[..., 0:1])*width).flatten()
    gt_heights = ((gt_boxes[..., 3:4] - gt_boxes[..., 1:2])*height).flatten()
    dt_widths = ((dt_boxes[..., 2:3] - dt_boxes[..., 0:1])*width).flatten()
    dt_heights = ((dt_boxes[..., 3:4] - dt_boxes[..., 1:2])*height).flatten()

    gt_modify = np.transpose(
        np.nonzero(((gt_widths<clamp)+(gt_heights<clamp)))).flatten()
    dt_modify = np.transpose(
        np.nonzero(((dt_widths<clamp)+(dt_heights<clamp)))).flatten()

    if len(gt_boxes):
        gt_boxes[gt_modify, 2:3] = gt_boxes[gt_modify, 0:1] + clamp/width
        gt_boxes[gt_modify, 3:4] = gt_boxes[gt_modify, 1:2] + clamp/height
        instances['gt_instance']['boxes'] = gt_boxes
    if len(dt_boxes):
        dt_boxes[dt_modify, 2:3] = dt_boxes[dt_modify, 0:1] + clamp/width
        dt_boxes[dt_modify, 3:4] = dt_boxes[dt_modify, 1:2] + clamp/height
        instances['dt_instance']['boxes'] = dt_boxes
    return instances

def ignore_boxes(instances, ignore):
    """
    This function ignores the boxes with dimensions less than the ignore 
    parameter provided. 

    Parameters
    ----------
        instances: dict
            This contains the ground truth and the detection data.
            See README.md (Method Parameters Format) for more information.

        ignore: int
            The dimension pixels threshold to ignore. Any boxes with width 
            and height less than this value will be ignored and filtered out.

    Returns
    -------
        instances: dict
            This is the updated instances data which filtered out the boxes.

    Raises
    ------
        None
    """
    height = instances.get('gt_instance').get('height')
    width = instances.get('gt_instance').get('width')
    gt_boxes = instances.get('gt_instance').get('boxes')
    gt_labels = instances.get('gt_instance').get('labels')  
    dt_boxes = instances.get('dt_instance').get('boxes')
    dt_labels = instances.get('dt_instance').get('labels')
    scores = instances.get('dt_instance').get('scores')

    gt_widths = ((gt_boxes[..., 2:3] - gt_boxes[..., 0:1])*width).flatten()
    gt_heights = ((gt_boxes[..., 3:4] - gt_boxes[..., 1:2])*height).flatten()
    dt_widths = ((dt_boxes[..., 2:3] - dt_boxes[..., 0:1])*width).flatten()
    dt_heights = ((dt_boxes[..., 3:4] - dt_boxes[..., 1:2])*height).flatten()

    gt_keep = np.transpose(
        np.nonzero(((gt_widths>=ignore)*(gt_heights>=ignore)))).flatten()
    dt_keep = np.transpose(
        np.nonzero(((dt_widths>=ignore)*(dt_heights>=ignore)))).flatten()
    gt_boxes = gt_boxes[gt_keep]
    gt_labels =  gt_labels[gt_keep]
    dt_boxes = dt_boxes[dt_keep]
    dt_labels = dt_labels[dt_keep]
    scores = scores[dt_keep]

    instances['gt_instance']['boxes'] = gt_boxes
    instances['gt_instance']['labels'] = gt_labels
    instances['dt_instance']['boxes'] = dt_boxes
    instances['dt_instance']['labels'] = dt_labels
    instances['dt_instance']['scores'] = scores
    return instances

def nan_to_last_num(process_array):
    """
    This function replaces all NAN values with the last valid number. If all
    values are NaN, then all elements are replaced with zeros.

    Parameters
    ----------
        process_array: np.ndarray
            This is the array to replace NaN values with the last 
            acceptable value.

    Returns
    -------
        process_array: np.ndarray
            The same array but with NaN replaced with last acceptable values.
            Otherwise, all elements are replaced with zeros if all elements are
            NaN.

    Raises
    ------
        None
    """

    try:
        # Find the maximum index where the value is not a NaN.
        precision_repeat_id = np.max(
            np.argwhere(
                np.logical_not(
                    np.isnan(process_array))).flatten())
        # NaN values should be replace with the last acceptable value.
        process_array = np.nan_to_num(
            process_array,
            nan=process_array[int(precision_repeat_id)]
        )

    except ValueError:
        # The whole array are nans just convert back to zero.
        process_array[np.isnan(process_array)] = 0.

    return process_array

def match_gt_dt(gt_boxes, dt_boxes, metric='iou'):
    """
    This function is version 2 of the matching algorithm incorporates
    recursive calls to perform rematching of ground truth that were 
    unmatched due to duplicative matches, but the rematching is based on the
    next best IoU. This function attempts a best-fit of
    predictions to ground truths.
    Unit-test for this method is defined under:
        file: test/test_metrics.py
        function: test_match_gt_dt

    Parameters
    ----------
        gt_boxes: list or np.ndarray
            A list of ground truth boxes [[x1, y1, x2, y2]...].

        dt_boxes: list or np.ndarray
            A list of prediction boxes [[x1, y1, x2, y2]...].

    Returns
    -------
       indices : list
            This contains indices of the matches, extra predictions,
            missed ground truths, and
            IoU values for each match.

            * matches [[detection index, ground truth index],
                    [detection index, ground truth index], ...]
            * extras [detection index, detection index, ...]
            * missed [ground truth index, ground truth index, ...]

    Raises
    ------
        MatchingAlgorithmException
            This function will raise an exception if the method finds
            invalid values for IoU and ground truth index such as -1
    """
    
    # This contains the IoUs of each detection.
    iou_list = np.zeros(len(dt_boxes))
    # Row is ground truth, columns is detection IoUs
    iou_grid = np.zeros((len(gt_boxes), len(dt_boxes)))
    index_matches = list()

    def compare_matches(dti, gti, iou):
        """
        This function checks if duplicate matches exists. A duplicate match
        is when the same detection is being matched to more than one 
        ground truth. The IoUs are compared and the better IoU is the true
        match and the ground truth of the other match is then rematch 
        to the next best IoU, but it performs a recursive call to check
        if the next best IoU also generates a duplicate match.

        Parameters
        ----------
            dti: int
                The detection index being matched to the current ground truth.
            
            gti: int
                The current ground truth matched to the detection.

            iou: float
                The current best IoU that was computed for the current ground
                truth against all detections.

        Returns
        -------
            None

        Raises
        ------
            MatchingAlgorithmException:
                This function will raise an exception if a duplicate match
                was left unchecked and was not rematched. 
        """

        twice_matched = [(d,g) for d, g in index_matches if d == dti]
        if len(twice_matched) == 1:
            # Compare the IoUs between duplicate matches.
            dti, pre_gti = twice_matched[0]
            if iou > iou_list[dti]:
                index_matches.remove((dti, pre_gti))
                iou_list[dti] = iou
                index_matches.append((dti, gti))

                # Rematch pre_gti
                iou_grid[pre_gti][dti] = 0.
                dti = np.argmax(iou_grid[pre_gti])
                iou = max(iou_grid[pre_gti])
                if iou > 0.:
                    compare_matches(dti, pre_gti, iou)
            else:
                # Rematch gti
                iou_grid[gti][dti] = 0.
                dti = np.argmax(iou_grid[gti])
                iou = max(iou_grid[gti])
                if iou > 0.:
                    compare_matches(dti, gti, iou)
        elif len(twice_matched) == 0:
            if iou > 0.:
                iou_list[dti] = iou
                index_matches.append((dti, gti))
        else:
            raise MatchingAlgorithmException(
                "Duplicate matches were unchecked.") 

    if len(gt_boxes) > 0:
        for gti, gt in enumerate(gt_boxes):
            if len(dt_boxes):
                for dti, dt in enumerate(dt_boxes):
                    # Find the IoUs of each prediction against the current gt.
                    if metric.lower() == 'iou':
                        iou_grid[gti][dti] = \
                            bb_intersection_over_union(dt, gt)
                    elif metric.lower() == 'centerpoint':
                        iou_grid[gti][dti] = \
                            1 - center_point_distance(dt, gt)
                    else:
                        raise MatchingAlgorithmException("Unknown matching " + 
                                    "matching metric specified.")
            else:
                return [index_matches, [], list(range(0, len(gt_boxes))), []]
                         
            # A potential match is the detection that produced the highest IoU.
            dti = np.argmax(iou_grid[gti])
            iou = max(iou_grid[gti])
            compare_matches(dti, gti, iou)
               
        # Find the unmatched predictions
        index_unmatched_dt = list(range(0, len(dt_boxes)))
        index_unmatched_gt = list(range(0, len(gt_boxes)))
        for match in index_matches:
            index_unmatched_dt.remove(match[0])
            index_unmatched_gt.remove(match[1])                    
    else:
        index_unmatched_dt = list(range(0, len(dt_boxes)))
        index_unmatched_gt = list()
    return [index_matches, index_unmatched_dt, index_unmatched_gt, iou_list]

def match_dt_gt(gt_boxes, dt_boxes, metric='iou'):
    """
    This function is version 1 of the matching algorithm. This function is 
    lacking in the aspect of performing rematching of detections on the 
    next best IoU.
    This function attempts a best-fit of
    predictions to ground truths.
    Unit-test for this method is defined under:
        file: test/test_metrics.py
        function: test_match_dt_gt

    Parameters
    ----------
        gt_boxes: list or np.ndarray
            A list of ground truth boxes [[x1, y1, x2, y2]...].

        dt_boxes: list or np.ndarray
            A list of prediction boxes [[x1, y1, x2, y2]...].

    Returns
    -------
       indices : list
            This contains indices of the matches, extra predictions,
            missed ground truths, and
            IoU values for each match.

            * matches [[detection index, ground truth index],
                    [detection index, ground truth index], ...]
            * extras [detection index, detection index, ...]
            * missed [ground truth index, ground truth index, ...]

    Raises
    ------
        MatchingAlgorithmException
            This function will raise an exception if the method finds
            invalid values for IoU and ground truth index such as -1
    """

    # Rows is prediction, columns is ground truth
    iou_grid, iou_list = list(), list()
    index_matches, index_extra_dt = list(), list()

    if len(gt_boxes) > 0:
        for dti, dt in enumerate(dt_boxes):
            iou, gti = -1, -1
            iou_row = list()
            # get the best IOU and its GT index for the detection
            for id, gt in enumerate(gt_boxes):
                if metric.lower() == 'iou':
                    t_iou = bb_intersection_over_union(dt, gt)
                elif metric.lower() == 'centerpoint':
                    t_iou = 1 - center_point_distance(dt, gt)
                else:
                    raise MatchingAlgorithmException("Unknown matching " + 
                                "matching metric specified.")
                iou_row.append(t_iou)
                if t_iou > iou:
                    iou = t_iou
                    gti = id

            iou_grid.append(iou_row)

            # At this point, (dti, gti) is the coordinates
            # for the best IOU for the detection.
            # If IOU or GTI is -1, you have problems.
            if iou == -1 or gti == -1:
                raise MatchingAlgorithmException(
                    iou, gti
                )

            iou_list.append(iou)

            # if the ground truth as already been matched, we need to see if
            # the new IOU score is higher.  If so, remove the old match,
            # add this match, and note the old match as a duplicate.
            # Otherwise, add this as a duplicate of the better match.
            if gti in [g for _, g in index_matches if g == gti]:

                for d, g in index_matches:
                    if g == gti:
                        break

                # if the new IOU is better than the previous IOU, remove
                # the old tuple, add the new one and mark the old detection as
                # a duplicate
                if iou > iou_list[d]:
                    index_matches.remove((d, gti))
                    index_matches.append((dti, gti))
                    index_extra_dt.append(d)

                # if the new detection IOU is worse, it's a dup of a better one
                else:
                    index_extra_dt.append(dti)

            # if the GT is not already matched, add it to the GT index list and
            # add the DT,GT index pair to the DT-GT index matching list
            else:
                index_matches.append((dti, gti))

        # Find the missed predictions by removing the indices that were
        # predicted.
        index_missed_gt = list(range(0, len(gt_boxes)))
        for match in index_matches:
            index_missed_gt.remove(match[1])

        # Sort the indices from smallest to largest to match box numbering [0],
        # [1] .... in original output.
        index_extra_dt.sort()
        index_missed_gt.sort()
        # Only sort by the second element of each list [[0,3], [1,2], [4,8]] ->
        # [[1,2], [0,3], [4,8]].
        index_matches.sort(key=lambda x: x[1])

    else:
        index_extra_dt = list(range(0, len(dt_boxes)))
        index_missed_gt = list()

    return [index_matches, index_extra_dt, index_missed_gt, iou_list]