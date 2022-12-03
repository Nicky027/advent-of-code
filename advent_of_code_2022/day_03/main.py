from rucksack import get_common_elements, get_elf_groups, get_elf_group_badges
from alphabet import get_letter_priorities


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    rucksacks = [input.replace("\n", "") for input in inputs]
    priorities = get_letter_priorities()

    # part 1
    common_elements = get_common_elements(rucksacks)
    common_element_priorities = [
        priorities[letter] for letter in common_elements
    ]
    print(sum(common_element_priorities))

    # part 2
    elf_groups = get_elf_groups(rucksacks)
    elf_group_badges = get_elf_group_badges(elf_groups)
    badge_priorities = [priorities[letter] for letter in elf_group_badges]
    print(sum(badge_priorities))


if __name__ == "__main__":
    main()
