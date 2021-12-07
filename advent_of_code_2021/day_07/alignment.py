def fuel_cost(crabs, position):
    return sum(map(lambda x: abs(x - position), crabs))


def advanced_fuel_cost(crabs, position):
    return sum(
        map(lambda x: advanced_fuel_consumption(abs(x - position)), crabs)
    )


def advanced_fuel_consumption(distance):
    return int(((distance) * (distance + 1)) / 2)
