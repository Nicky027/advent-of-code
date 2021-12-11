import numpy as np


def parse_inputs(inputs):
    return np.array([[int(x) for x in input] for input in inputs])


def step(energies):
    energies = energies + 1

    has_flashed = []
    to_flash = list(np.argwhere(energies == 10))

    while to_flash:
        to_flash_next = []
        for octopus_index in to_flash:
            if list(octopus_index) not in has_flashed:
                energies = increment_neighbours(octopus_index, energies)
                has_flashed.append(list(octopus_index))
                to_flash_next.append(list(np.argwhere(energies == 10)))
        to_flash = [
            index for flash_list in to_flash_next for index in flash_list
        ]
    return normalise_energies(energies)


def increment_neighbours(index, energies):
    x = index[0]
    y = index[1]
    energies[x, y] += 1
    if x - 1 >= 0:
        energies[x - 1, y] += 1
        if y - 1 >= 0:
            energies[x - 1, y - 1] += 1
        if y + 1 < energies.shape[1]:
            energies[x - 1, y + 1] += 1
    if x + 1 < energies.shape[1]:
        energies[x + 1, y] += 1
        if y - 1 >= 0:
            energies[x + 1, y - 1] += 1
        if y + 1 < energies.shape[1]:
            energies[x + 1, y + 1] += 1
    if y - 1 >= 0:
        energies[x, y - 1] += 1
    if y + 1 < energies.shape[1]:
        energies[x, y + 1] += 1
    return energies


def normalise_energies(energies):
    return np.where(energies > 9, 0, energies)
