import numpy as np


def get_neighbours(i, j, seats):
    return seats[
        max(i - 1, 0):min(seats.shape[0], i + 2),
        max(j - 1, 0):min(seats.shape[1], j + 2),
    ]


def get_new_seats(seats):
    new_seats = seats.copy()

    for i in range(new_seats.shape[0]):
        for j in range(new_seats.shape[1]):
            neighbours = get_neighbours(i, j, seats)

            if seats[i, j] == "L":
                occupied = (neighbours == "#").sum()
                if occupied == 0:
                    new_seats[i, j] = "#"

            elif seats[i, j] == "#":
                occupied = (neighbours == "#").sum() - 1
                if occupied >= 4:
                    new_seats[i, j] = "L"
    return new_seats


def stabilize(seats):
    new_seats = get_new_seats(seats)
    if np.all(new_seats == seats):
        return seats
    else:
        return stabilize(new_seats)


def get_neighbours_v2(i, j, seats):
    top_left = seats[0:i+1, 0:j+1]
    bottom_left = seats[i:, 0:j+1]
    top_right = seats[0:i+1, j:]
    bottom_right = seats[i:, j:]

    arrays = [
            np.flip(seats[i, 0:j+1]),
            seats[i, j:],
            np.flip(seats[0:i+1, j]),
            seats[i:, j],
            np.fliplr(np.flipud(top_left)).diagonal(),
            np.fliplr(bottom_left).diagonal(),
            np.flipud(top_right).diagonal(),
            bottom_right.diagonal(),
    ]

    neighbours = []

    for array in arrays:
        
        for point in array[1:]:
            if point == "#" or point == "L":
                neighbours.append(point)
                break

    return np.array(neighbours)


def get_new_seats_v2(seats):
    new_seats = seats.copy()

    for i in range(new_seats.shape[0]):
        for j in range(new_seats.shape[1]):
            neighbours = get_neighbours_v2(i, j, seats)

            occupied = (neighbours == "#").sum()

            if seats[i, j] == "L" and occupied == 0:
                new_seats[i, j] = "#"

            elif seats[i, j] == "#" and occupied >= 5:
                new_seats[i, j] = "L"

    return new_seats


def stabilize_v2(seats):
    new_seats = get_new_seats_v2(seats)
    if np.all(new_seats == seats):
        return seats
    else:
        return stabilize_v2(new_seats)
