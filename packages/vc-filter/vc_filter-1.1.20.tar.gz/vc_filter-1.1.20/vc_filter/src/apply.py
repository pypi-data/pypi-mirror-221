# Jul-23-2023
# vc_filter.py

import cv2 as cv
import numpy as np

from vc_filter.src.others import sobel_accum


def apply(image):

    # convert color to grayscale
    if len(image.shape) != 2:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    rows, cols = image.shape
    image_max_size = max(rows, cols)
    size_dft = 256
    while image_max_size > size_dft:
        size_dft *= 2

    width_dft = size_dft
    height_dft = size_dft

    """  Sobel based filter  """
    # ---------------------------------------------------------
    dft_filter_accum = sobel_accum(height_dft, width_dft)
    # ---------------------------------------------------------

    """  Image  """
    # ---------------------------------------------------------
    array_image = np.zeros((height_dft, width_dft), dtype='float32')

    x0 = (width_dft - cols) // 2
    y0 = (height_dft - rows) // 2

    array_image[y0:y0 + rows, x0:x0 + cols] = image[0::, 0::]

    dft_image = cv.dft(array_image, flags=cv.DFT_COMPLEX_OUTPUT)

    # DFT{Image}
    dft_image_shift = np.fft.fftshift(dft_image)
    # ---------------------------------------------------------

    """  DFT{Filter} * DFT{Image}  """
    # -----------------------------------------
    dft_product_shift = np.empty((height_dft, width_dft, 2), dtype='float32')

    x1 = dft_filter_accum[:, :, 0]
    y1 = dft_filter_accum[:, :, 1]

    x2 = dft_image_shift[:, :, 0]
    y2 = dft_image_shift[:, :, 1]

    dft_product_shift[:, :, 0] = (x1 * x2) - (y1 * y2)
    dft_product_shift[:, :, 1] = (x1 * y2) + (x2 * y1)
    # -----------------------------------------

    """  Inverse DFT """
    # -----------------------------------------
    inverse_dft = cv.idft(dft_product_shift)

    re = inverse_dft[:, :, 0]
    re[re < 0.0] = 0.0
    # -----------------------------------------

    #  Get filtered image
    # -----------------------------------------
    image_array = np.empty((rows, cols), dtype='float32')

    x0 = (width_dft - cols) // 2
    y0 = (height_dft - rows) // 2

    image_array[::, ::] = re[y0:y0 + rows, x0:x0 + cols]
    # -----------------------------------------

    #  Remove "border noise"
    # -----------------------------------------
    border = 8
    image_array[0:border, 0:cols] = 0.0
    image_array[rows - border:rows, 0:cols] = 0.0
    image_array[0:rows, 0:border] = 0.0
    image_array[0:rows, cols - border:cols] = 0.0
    # -----------------------------------------

    #  Normalization
    # -----------------------------------------
    image_norm = np.zeros((rows, cols), dtype=np.float32)
    cv.normalize(image_array, image_norm, 0, 255, cv.NORM_MINMAX)
    image_array_8u = np.uint8(image_norm)
    # -----------------------------------------

    #  Both flips
    image_edges = cv.flip(image_array_8u, -1)

    return image_edges
