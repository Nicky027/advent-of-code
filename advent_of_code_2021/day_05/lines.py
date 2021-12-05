import numpy as np
from collections import Counter


def get_lines(inputs, diagonals=False):
    lines = []
    for input in inputs:
        parsed_input = input.split(" -> ")
        end_points = [
            list(map(lambda x: int(x), p.split(","))) for p in parsed_input
        ]
        line_gradient = get_line_gradient(end_points)
        passed_points = []
        if line_gradient == np.Inf:
            x = end_points[0][0]
            min_y = min([end_points[0][1], end_points[1][1]])
            max_y = max([end_points[0][1], end_points[1][1]])
            for y in range(min_y, max_y + 1):
                passed_points.append((x, y))
        elif line_gradient == 0:
            y = end_points[0][1]
            min_x = min([end_points[0][0], end_points[1][0]])
            max_x = max([end_points[0][0], end_points[1][0]])
            for x in range(min_x, max_x + 1):
                passed_points.append((x, y))

        if diagonals and abs(line_gradient) == 1:
            if end_points[0][0] <= end_points[1][0]:
                x = end_points[0][0]
                y = end_points[0][1]
                max_x = end_points[1][0]
            else:
                x = end_points[1][0]
                y = end_points[1][1]
                max_x = end_points[0][0]

            while x <= max_x:
                passed_points.append((x, y))
                x += 1
                if line_gradient > 0:
                    y += 1
                else:
                    y -= 1
        lines.append(passed_points)
    return lines


def get_point_crossings(lines):
    points_crossed = [p for line in lines for p in line]
    return dict(Counter(points_crossed))


def get_line_gradient(end_points):
    # vertical line
    if end_points[0][0] == end_points[1][0]:
        return np.Inf
    # horizontal line
    elif end_points[0][1] == end_points[1][1]:
        return 0
    # sloped line (dy / dx)
    else:
        return (end_points[0][1] - end_points[1][1]) / (
            end_points[0][0] - end_points[1][0]
        )
