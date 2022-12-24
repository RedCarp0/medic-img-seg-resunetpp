import numpy as np
from scipy import spatial


def dice_coeff(im1, im2, empty_score=1.0):
    """Calculates the dice coefficient for the images"""

    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")


    ### (lzj) note that the label 0 is predicted value instead of label 1.
    # im1 = im1 > 0.5
    # im2 = im2 > 0.5
    im1 = im1 < 0.5
    im2 = im2 < 0.5

    im_sum = im1.sum() + im2.sum()
    if im_sum == 0:
        return empty_score

    # Compute Dice coefficient
    intersection = np.logical_and(im1, im2)
    #print(im_sum)

    return 2. * intersection.sum() / im_sum


def numeric_score(prediction, groundtruth):
    """Computes scores:
    FP = False Positives
    FN = False Negatives
    TP = True Positives
    TN = True Negatives
    return: FP, FN, TP, TN"""


    ### (lzj) note that the label 0 is predicted value instead of label 1.
    # FP = np.float(np.sum((prediction == 1) & (groundtruth == 0)))
    # FN = np.float(np.sum((prediction == 0) & (groundtruth == 1)))
    # TP = np.float(np.sum((prediction == 1) & (groundtruth == 1)))
    # TN = np.float(np.sum((prediction == 0) & (groundtruth == 0)))
    FP = np.float(np.sum((prediction == 0) & (groundtruth == 1)))
    FN = np.float(np.sum((prediction == 1) & (groundtruth == 0)))
    TP = np.float(np.sum((prediction == 0) & (groundtruth == 0)))
    TN = np.float(np.sum((prediction == 1) & (groundtruth == 1)))

    return FP, FN, TP, TN


def accuracy_score(prediction, groundtruth):
    """Getting the accuracy of the model"""

    FP, FN, TP, TN = numeric_score(prediction, groundtruth)
    N = FP + FN + TP + TN
    accuracy = np.divide(TP + TN, N)
    precision = np.divide(TP, TP + FP)
    recall = np.divide(TP, TP + FN)
    return accuracy*100.0, precision*100.0, recall*100.0


