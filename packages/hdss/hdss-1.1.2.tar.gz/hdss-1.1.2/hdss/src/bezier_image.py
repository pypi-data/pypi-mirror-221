import cv2 as cv

from hdss.src import glbl
from hdss.src.bezier_utils import evaluate_bezier


def bezier_image(image, points):

    curve = evaluate_bezier(points, 15)

    px, py = curve[:, 0], curve[:, 1]

    # Draw current curve
    # ---------------------------------------------------------
    for i in range(1, px.size):

        x1 = int(round(px[i-1]))
        y1 = int(round(py[i-1]))

        x2 = int(round(px[i]))
        y2 = int(round(py[i]))

        cv.line(image,
                (x1, y1), (x2, y2),
                glbl.line_color,
                glbl.line_thickness)
    # ---------------------------------------------------------
