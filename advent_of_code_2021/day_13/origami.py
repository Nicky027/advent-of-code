import numpy as np

def parse_inputs(inputs):
    dots = []
    fold_lines = []
    for input in inputs:
        if input == "":
            continue
        elif input.startswith("fold"):
            fold_line = input.split("=")
            fold_lines.append((fold_line[0][-1], int(fold_line[1])))
        else:
            dots.append(tuple(int(i) for i in input.split(",")))
    return set(dots), fold_lines


def fold(dots, line):
    axis = line[0]
    new_dots = set()

    if axis == "y":
        y = line[1]
        for dot in dots:
            if dot[1] < y:
                new_dots.add(dot)
            else:
                new_dots.add((dot[0], 2 * y - dot[1]))

    if axis == "x":
        x = line[1]
        for dot in dots:
            if dot[0] < x:
                new_dots.add(dot)
            else:
                new_dots.add((2 * x - dot[0], dot[1]))

    return new_dots

def dots_to_code(dots):
    max_x = np.max([dot[0] for dot in dots])
    max_y = np.max([dot[1] for dot in dots])
    code = np.full((max_x+1, max_y+1), ' ')
    for dot in dots:
        code[dot[0], dot[1]] = 'W'
    return code.T
