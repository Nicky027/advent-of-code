import numpy as np
from seating import stabilize, stabilize_v2


def main():
    with open("input.txt", "r") as file:
        seats = file.readlines()

    seating_matrix = np.array([list(x.replace("\n", "")) for x in seats])

    print((stabilize(seating_matrix) == "#").sum())
    print((stabilize_v2(seating_matrix) == "#").sum())


if __name__ == "__main__":
    main()
