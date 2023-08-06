import random

from hdss.src import glbl


def random_noise(scale_factor):

    half = scale_factor * glbl.bezier_noise_param / 2.0

    return random.uniform(-half, half)
