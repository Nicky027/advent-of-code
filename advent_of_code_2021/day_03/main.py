import numpy as np


def filter_most_common(xs, i):
    first_bits = [int(x[i]) for x in xs]
    if np.mean(np.array(first_bits)) >= 0.5:
        most_common = "1"
    else:
        most_common = "0"
    filtered_xs = [x for x in xs if x[i] == most_common]

    return filtered_xs


def filter_least_common(xs, i):
    first_bits = [int(x[i]) for x in xs]
    if np.mean(np.array(first_bits)) >= 0.5:
        least_common = "0"
    else:
        least_common = "1"
    filtered_xs = [x for x in xs if x[i] == least_common]

    return filtered_xs


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    # part 1
    gamma = []
    epsilon = []

    for i in range(len(inputs[0])):
        x = [int(input[i]) for input in inputs]
        if np.mean(np.array(x)) > 0.5:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    g = int("".join(gamma), 2)
    e = int("".join(epsilon), 2)
    print(g, e, g * e)

    # part 2
    o2_list = inputs
    i = 0
    while len(o2_list) > 1:
        o2_list = filter_most_common(o2_list, i)
        i = i + 1

    co2_list = inputs
    i = 0
    while len(co2_list) > 1:
        co2_list = filter_least_common(co2_list, i)
        i = i + 1

    o2 = int(o2_list[0], 2)
    co2 = int(co2_list[0], 2)
    print(o2, co2, o2 * co2)


if __name__ == "__main__":
    main()
