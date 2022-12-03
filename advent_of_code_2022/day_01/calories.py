from typing import List


def get_sums(inputs: List) -> List:
    elf_sums = []
    elf_sum = []
    for input in inputs:
        if input == "\n":
            elf_sums.append(sum(elf_sum))
            elf_sum = []
        else:
            elf_sum.append(int(input))
    elf_sums.append(sum(elf_sum))
    return elf_sums
