import numpy as np
import pandas as pd
import scipy as scp
import matplotlib as mpl
from skimage import morphology
import cv2
import matplotlib.pyplot as pyplot
%matplotlib inline
def bckgrnd_correc_rect(image, row_len, col_len):

    """Background correction using a rectangular structuring element. This function uses white_tophat from
    skimage.morphology to return image minus the morphological opening obtained from the structuring element."""

    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')

    # Checking the right data type for the row length of the rectangular structuring element
    assert type(row_len) == float, ('Wrong data type', 'row length must be a float')

    # Checking the right data type for the column length of the rectangular structuring element
    assert type(col_len) == float, ('Wrong data type', 'column length must be a float')

    # background corrrection
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.rectangle(row_len,col_len))

    # plotting image
    plt.gray()
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()

    return image_bckgrnd_corrected
def bckgrnd_correc_sq(image, length):

    """Background correction using a square structuring element. This function uses white_tophat from
    skimage.morphology to return image minus the morphological opening obtained from the structuring element."""

    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')

    # Checking the right data type for the length of the square structuring element
    assert type(length) == float, ('Wrong data type', 'length of the square structuring element must be a float')

    # background correction
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.square(length))

    # plotting image
    plt.gray()
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()

    return image_bckgrnd_corrected
def bckgrnd_correc_disk(image, radius):

    """Background correction using a disk structuring element. This function uses white_tophat from
    skimage.morphology to return image minus the morphological opening obtained from the structuring element."""

    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')

    # Checking the right data type for the length of the square structuring element
    assert type(radius) == float, ('Wrong data type', 'radius of the disk structuring element must be a float')

    # background correction
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.disk(radius))

    # plotting image
    plt.gray()
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()

    return image_bckgrnd_corrected


def convert_to_grayscale(image):

    """Converting the image to grayscale - where minimum pixel value is 0.0 and maximum pixel value is 1.0"""

    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')

    # converting to grayscale
    dst = np.zeros(image.shape)
    image_gray = cv2.normalize(image, dst, 0.0, 1.0, cv2.NORM_MINMAX)

    # plotting the image
    plt.gray()
    plt.imshow(image_gray)
    plt.colorbar()

    return image_gray
