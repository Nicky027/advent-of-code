from typing import List, Tuple


def update_position(
    x: int, y: int, commands: List[str], steering_method="Part 1", aim: int = 0
) -> Tuple[int, int]:
    for command in commands:
        split_command = command.split(" ")
        direction = split_command[0]
        units = int(split_command[1])

        if steering_method == "Part 1":
            if direction == "forward":
                x += units

            elif direction == "down":
                y += units

            elif direction == "up":
                y -= units

        elif steering_method == "Part 2":
            if direction == "forward":
                x += units
                y += units * aim

            if direction == "down":
                aim += units

            if direction == "up":
                aim -= units

    return x, y
