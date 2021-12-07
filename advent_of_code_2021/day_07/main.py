import numpy as np
import alignment as a


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    crabs = [int(x) for input in inputs for x in input.split(",")]

    min_position = min(crabs)
    max_position = max(crabs)

    # part 1
    optimal_fuel = np.Inf
    optimal_position = None
    for i in range(min_position, max_position + 1):
        fuel = a.fuel_cost(crabs, i)
        if fuel < optimal_fuel:
            optimal_position = i
            optimal_fuel = fuel
    print(optimal_position, optimal_fuel)

    # part 2
    optimal_fuel = np.Inf
    optimal_position = None
    for i in range(min_position, max_position + 1):
        fuel = a.advanced_fuel_cost(crabs, i)
        if fuel < optimal_fuel:
            optimal_position = i
            optimal_fuel = fuel
    print(optimal_position, optimal_fuel)


if __name__ == "__main__":
    main()
