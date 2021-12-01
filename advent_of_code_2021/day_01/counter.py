from typing import List


def count_increasing(numbers: List[int]) -> int:
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
    return count
