import cv2 as cv
import numpy as np
import random

from hdss.src import glbl


def set_persp_transform():

    if not glbl.perspective_flag:

        glbl.x_tr_in = glbl.image_size
        glbl.y_tr_in = 0

        glbl.x_tl_in = 0
        glbl.y_tl_in = 0

        glbl.x_bl_in = 0
        glbl.y_bl_in = glbl.image_size

        glbl.x_br_in = glbl.image_size
        glbl.y_br_in = glbl.image_size

        matrix = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

        return matrix

    # Points order: top-right, top-left, bottom-left, bottom-right

    # IN
    # -----------------------------------------------------
    random.seed(None)

    glbl.x_tr_in = glbl.image_size + random_persp_shift()
    glbl.y_tr_in = -random_persp_shift()

    glbl.x_tl_in = -random_persp_shift()
    glbl.y_tl_in = -random_persp_shift()

    glbl.x_bl_in = -random_persp_shift()
    glbl.y_bl_in = glbl.image_size + random_persp_shift()

    glbl.x_br_in = glbl.image_size + random_persp_shift()
    glbl.y_br_in = glbl.image_size + random_persp_shift()

    """
    # Demo
    glbl.x_tr_in = 110
    glbl.y_tr_in = -10

    glbl.x_tl_in = -40
    glbl.y_tl_in = -45

    glbl.x_bl_in = -4
    glbl.y_bl_in = 145

    glbl.x_br_in = 140
    glbl.y_br_in = 105
    """
    # -----------------------------------------------------

    # OUT
    # ---------------------------------------------------------
    glbl.x_tr_out = glbl.image_size
    glbl.y_tr_out = 0

    glbl.x_tl_out = 0
    glbl.y_tl_out = 0

    glbl.x_bl_out = 0
    glbl.y_bl_out = glbl.image_size

    glbl.x_br_out = glbl.image_size
    glbl.y_br_out = glbl.image_size
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    pts1 = np.float32([[glbl.x_tr_in, glbl.y_tr_in], [glbl.x_tl_in, glbl.y_tl_in],
                       [glbl.x_bl_in, glbl.y_bl_in], [glbl.x_br_in, glbl.y_br_in]])

    pts2 = np.float32([[glbl.x_tr_out, glbl.y_tr_out], [glbl.x_tl_out, glbl.y_tl_out],
                       [glbl.x_bl_out, glbl.y_bl_out], [glbl.x_br_out, glbl.y_br_out]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    # ---------------------------------------------------------

    return matrix


def random_persp_shift():
    return random.uniform(0.0, glbl.image_size / 2.0)


def point_persp_transform(matrix, x_in, y_in):
    x_out = matrix[0, 0] * x_in + matrix[0, 1] * y_in + matrix[0, 2]
    y_out = matrix[1, 0] * x_in + matrix[1, 1] * y_in + matrix[1, 2]
    z_out = matrix[2, 0] * x_in + matrix[2, 1] * y_in + matrix[2, 2]

    x_out = x_out / z_out
    y_out = y_out / z_out

    return x_out, y_out


def print_persp_transform(matrix):
    print()
    print(f'matrix[0, 0] = {matrix[0, 0]}')
    print(f'matrix[0, 1] = {matrix[0, 1]}')
    print(f'matrix[0, 2] = {matrix[0, 2]}')

    print()
    print(f'matrix[1, 0] = {matrix[1, 0]}')
    print(f'matrix[1, 1] = {matrix[1, 1]}')
    print(f'matrix[1, 2] = {matrix[1, 2]}')

    print()
    print(f'matrix[2, 0] = {matrix[2, 0]}')
    print(f'matrix[2, 1] = {matrix[2, 1]}')
    print(f'matrix[2, 2] = {matrix[2, 2]}')


def print_persp_rect():
    # ---------------------------------------------------------
    x1_in = glbl.x_tr_in
    y1_in = glbl.y_tr_in

    x2_in = glbl.x_tl_in
    y2_in = glbl.y_tl_in

    x3_in = glbl.x_bl_in
    y3_in = glbl.y_bl_in

    x4_in = glbl.x_br_in
    y4_in = glbl.y_br_in
    # ---------------------------------------------------------
    x1_out = glbl.x_tr_out
    y1_out = glbl.y_tr_out

    x2_out = glbl.x_tl_out
    y2_out = glbl.y_tl_out

    x3_out = glbl.x_bl_out
    y3_out = glbl.y_bl_out

    x4_out = glbl.x_br_out
    y4_out = glbl.y_br_out
    # ---------------------------------------------------------
    print(f'\nPerspective rectangles:')
    print(f'---------------------------')
    print(f'x1_in = {x1_in}\t y1_in = {y1_in}')
    print(f'x2_in = {x2_in}\t y2_in = {y2_in}')
    print(f'x3_in = {x3_in}\t y3_in = {y3_in}')
    print(f'x4_in = {x4_in}\t y4_in = {y4_in}')
    print()
    print(f'x1_out = {int(round(x1_out))}\t y1_out = {int(round(y1_out))}')
    print(f'x2_out = {int(round(x2_out))}\t y2_out = {int(round(y2_out))}')
    print(f'x3_out = {int(round(x3_out))}\t y3_out = {int(round(y3_out))}')
    print(f'x4_out = {int(round(x4_out))}\t y4_out = {int(round(y4_out))}')
    print(f'---------------------------')
    # ---------------------------------------------------------
