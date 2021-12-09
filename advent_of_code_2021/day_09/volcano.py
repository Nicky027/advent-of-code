import numpy as np


def parse_inputs(inputs):
    lines = []
    for input in inputs:
        lines.append([int(x) for x in input])
    return np.array(lines)


def get_neighbours(points):
    point_neighbours = []
    for i in range(points.shape[0]):
        for j in range(points.shape[1]):
            neighbours, _ = get_point_neighbours((i, j), points)
            point_neighbours.append(((i, j), points[i, j], neighbours))
    return point_neighbours


def get_point_neighbours(index, points):
    i = index[0]
    j = index[1]
    neighbours = []
    neighbour_indexes = []
    if i - 1 >= 0:
        neighbours.append(points[i - 1, j])
        neighbour_indexes.append((i - 1, j))
    if i + 1 < points.shape[0]:
        neighbours.append(points[i + 1, j])
        neighbour_indexes.append((i + 1, j))
    if j - 1 >= 0:
        neighbours.append(points[i, j - 1])
        neighbour_indexes.append((i, j - 1))
    if j + 1 < points.shape[1]:
        neighbours.append(points[i, j + 1])
        neighbour_indexes.append((i, j + 1))
    return neighbours, neighbour_indexes


def get_lowest_points(point_neighbours):
    lowest_points = []
    lowest_points_indexes = []
    for index, point, neighbours in point_neighbours:
        if point < min(neighbours):
            lowest_points.append(point)
            lowest_points_indexes.append(index)
    return lowest_points, lowest_points_indexes


def get_basins(points, indexes):
    point_basins = []
    for i in range(points.shape[0]):
        for j in range(points.shape[1]):
            if (i, j) not in indexes:
                continue
            basin_indexes = []
            get_point_basin((i, j), points, basin_indexes)
            point_basins.append(((i, j), points[i, j], set(basin_indexes)))
    return point_basins


def get_point_basin(index, points, basin_indexes):
    point = points[index[0], index[1]]
    if point != 9 and sum([1 for i in basin_indexes if i == index]) <= 1:
        neighbours, neighbour_indexes = get_point_neighbours(index, points)
        for n, i in zip(neighbours, neighbour_indexes):
            if n != 9:
                basin_indexes.append(i)
                get_point_basin(i, points, basin_indexes)
