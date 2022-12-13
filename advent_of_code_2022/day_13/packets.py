from enum import Enum


def parse_inputs(inputs: list) -> list:
    pairs = []
    pair = []
    for input in inputs:
        parsed_input = input.replace("\n", "")
        if parsed_input == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(eval(parsed_input))
    pairs.append(pair)
    return pairs


class Outcome(Enum):
    LESS_THAN = 0
    GREATER_THAN = 1
    EQUAL = 2


def compare(x: list, y: list) -> Outcome:
    for i in range(len(x)):
        xi = x[i]

        if i < len(y):
            yi = y[i]
        else:
            return Outcome.GREATER_THAN

        if isinstance(xi, int) and isinstance(yi, int):
            if xi < yi:
                return Outcome.LESS_THAN
            elif xi > yi:
                return Outcome.GREATER_THAN
            else:
                continue

        if isinstance(xi, list) and isinstance(yi, list):
            result = compare(xi, yi)

        if isinstance(xi, int) and isinstance(yi, list):
            result = compare([xi], yi)

        if isinstance(xi, list) and isinstance(yi, int):
            result = compare(xi, [yi])

        if result in [Outcome.LESS_THAN, Outcome.GREATER_THAN]:
            return result

    if len(x) < len(y):
        return Outcome.LESS_THAN

    return Outcome.EQUAL


def get_right_pair_indices(pairs: list) -> list:
    right_pair_indices = []
    for i, pair in enumerate(pairs, 1):
        if compare(pair[0], pair[1]) == Outcome.LESS_THAN:
            right_pair_indices.append(i)
    return right_pair_indices


def sort_packets(packets: list) -> list:
    n = len(packets)
    in_order = True

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compare(packets[j], packets[j + 1]) == Outcome.GREATER_THAN:
                in_order = False
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

        if in_order:
            return
