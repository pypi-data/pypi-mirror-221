import sys
import cv2 as cv
import numpy as np

from shapes_recognition.src import cfg
from shapes_recognition.src.check_background import check_background


def get_column_data(list_in):

    column_data_width = cfg.calc_size
    column_data_height = cfg.calc_size * len(list_in)

    column_data = \
        np.zeros((column_data_height, column_data_width), dtype=np.uint8)

    n_row: int = 0
    for path in list_in:

        image = cv.imread(path, cv.IMREAD_GRAYSCALE)

        height = image.shape[0]
        width = image.shape[1]

        if height != cfg.cell_height or width != cfg.cell_width:
            print(f'\nERROR: ' + path + ' - incorrect size')
            sys.exit(1)

        image_resize = cv.resize(
            image,
            (cfg.calc_size, cfg.calc_size),
            cv.INTER_LANCZOS4)

        result = check_background(image_resize)
        if result == 0:
            print(f'\nERROR: ' + path + ' - unacceptable shape')
            sys.exit(1)

        image = np.invert(image_resize)
        image_norm = np.zeros((cfg.calc_size, cfg.calc_size), dtype=np.uint8)
        cv.normalize(image, image_norm, 0, 255, cv.NORM_MINMAX)

        shift_vert = n_row * cfg.calc_size

        column_data[
            shift_vert:shift_vert + cfg.calc_size:,
            0:cfg.calc_size:] = image_norm[0::, 0::]

        n_row += 1

    return column_data
