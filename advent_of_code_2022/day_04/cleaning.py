from typing import List, Set, Tuple


def parse_pair(pair: str) -> Tuple[Set, Set]:
    split_pair = pair.split(",")
    x1 = split_pair[0].split("-")
    x1_elements = set(range(int(x1[0]), int(x1[1]) + 1))
    x2 = split_pair[1].split("-")
    x2_elements = set(range(int(x2[0]), int(x2[1]) + 1))
    return x1_elements, x2_elements


def get_intersection(x1: Set, x2: Set) -> Set:
    return x1.intersection(x2)


def count_fully_contained_pairs(pairs: List) -> int:
    count = 0

    for pair in pairs:
        x1, x2 = parse_pair(pair)
        intersection = get_intersection(x1, x2)
        if len(intersection) == len(x1) or len(intersection) == len(x2):
            count += 1

    return count


def count_overlapping_pairs(pairs: List) -> int:
    count = 0

    for pair in pairs:
        x1, x2 = parse_pair(pair)
        intersection = get_intersection(x1, x2)
        if len(intersection) > 0:
            count += 1

    return count
