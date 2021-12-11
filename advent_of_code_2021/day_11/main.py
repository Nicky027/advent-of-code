import octopus as o
import numpy as np


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    energies = o.parse_inputs(inputs)

    # part 1
    flashes = 0
    for i in range(100):
        energies = o.step(energies)
        flashes += np.sum(energies == 0)
    print(flashes)

    # part 2
    energies = o.parse_inputs(inputs)
    step = 1
    while True:
        energies = o.step(energies)
        if np.all(energies == 0):
            break
        else:
            step += 1
    print(step)


if __name__ == "__main__":
    main()
