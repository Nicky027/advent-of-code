from typing import Dict


def get_letter_priorities() -> Dict:
    priorities = {}

    for priority, letter in enumerate(range(ord("a"), ord("z") + 1)):
        priorities[chr(letter)] = priority + 1

    for priority, letter in enumerate(range(ord("A"), ord("Z") + 1)):
        priorities[chr(letter)] = priority + 27

    return priorities
