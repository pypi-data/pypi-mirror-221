from hdss.src import glbl


def set_params(
        shape_size,
        number_of_shapes,
        perspective_flag,
        bezier_noise_param,
        line_color,
        line_thickness):

    glbl.image_size = shape_size
    glbl.n_shapes = number_of_shapes
    glbl.perspective_flag = perspective_flag
    glbl.bezier_noise_param = bezier_noise_param
    glbl.line_color = line_color
    glbl.line_thickness = line_thickness
