import volcano as vc
import numpy as np


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    points = vc.parse_inputs(inputs)

    # part 1
    point_neighbours = vc.get_neighbours(points)
    lowest_points, lowest_points_indexes = vc.get_lowest_points(
        point_neighbours
    )
    print(sum([i + 1 for i in lowest_points]))

    # part 2
    basin_sizes = []
    for b in vc.get_basins(points, lowest_points_indexes):
        basin_sizes.append(len(b[2]))
    basin_sizes.sort(reverse=True)
    print(np.product(basin_sizes[0:3]))


if __name__ == "__main__":
    main()
