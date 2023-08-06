import cv2 as cv
import numpy as np
from pathlib import Path

from hdss.src import glbl
from hdss.src.bezier_image import bezier_image
from hdss.src.set_persp_transform import set_persp_transform, point_persp_transform
from hdss.src.set_random_noise import random_noise


def create_shapes(dir_name, shape_name, *curves):

    for n_shape in range(glbl.n_shapes):
        create_shape(dir_name, n_shape, shape_name, *curves)


def create_shape(dir_name, n_shape, shape_name, *curves):
    # ---------------------------------------------------------
    height = glbl.image_size
    width = glbl.image_size
    channels = 3
    background = 255
    image = np.empty((height, width, channels), dtype=np.uint8)
    image.fill(background)
    # ---------------------------------------------------------
    scale_factor = np.float32(glbl.image_size) / np.float32(100)

    matrix_persp = (3, 3)
    matrix_persp = np.zeros(matrix_persp, dtype=np.float32)

    if glbl.perspective_flag:
        matrix_persp = set_persp_transform()
    # ---------------------------------------------------------
    for path_curve in curves:

        control_points = np.loadtxt(path_curve, delimiter=',')
        n_control_points = control_points.shape[0]

        control_points = scale_factor * control_points
        # -----------------------------------------------------

        # Perspective Transform
        # -----------------------------------------------------
        if glbl.perspective_flag:

            for n in range(n_control_points):
                x_in = control_points[n, 0]
                y_in = control_points[n, 1]

                x_out, y_out = \
                    point_persp_transform(matrix_persp, x_in, y_in)

                control_points[n, 0] = x_out
                control_points[n, 1] = y_out
        # -----------------------------------------------------

        # Random Noise
        # -----------------------------------------------------
        if glbl.bezier_noise_param != 0:
            for n in range(n_control_points):
                control_points[n, 0] = control_points[n, 0] + random_noise(scale_factor)
                control_points[n, 1] = control_points[n, 1] + random_noise(scale_factor)
        # -----------------------------------------------------

        bezier_image(image, control_points)

    temp = shape_name + '_' + str(n_shape) + '.png'
    path_shape = str(Path.cwd() / dir_name / temp)
    cv.imwrite(path_shape, image)
