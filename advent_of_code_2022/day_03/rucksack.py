from typing import List


def split_rucksack(rucksack: str):
    length = len(rucksack)
    compartment_1 = rucksack[0 : int(length / 2)]
    compartment_2 = rucksack[int(length / 2) :]

    return compartment_1, compartment_2


def find_common_element(x1, x2):
    return list(x1.intersection(x2))[0]


def get_common_elements(rucksacks: List) -> List:
    common_elements = []
    for rucksack in rucksacks:
        c1, c2 = split_rucksack(rucksack)
        common_elements.append(find_common_element(set(c1), set(c2)))
    return common_elements


def get_elf_groups(rucksacks: List, group_size: int = 3) -> List:
    groups = {}
    for i, rucksack in enumerate(rucksacks):
        group_number = int(i / group_size)
        if groups.get(group_number, []):
            groups[group_number].append(rucksack)
        else:
            groups[group_number] = [rucksack]

    return groups.values()


def get_elf_group_badges(elf_groups: List):
    badges = []
    for group in elf_groups:
        potential_badge = set(list(group[0]))
        for elf in group[1:]:
            potential_badge = potential_badge.intersection(list(elf))
        badges.append(list(potential_badge)[0])
    return badges
