from typing import List, Tuple


def parse_inputs(inputs: List, r: int) -> Tuple[List, List]:
    instructions = [
        [int(x[1]), int(x[3]), int(x[5])]
        for x in [
            input.replace("\n", "").split(" ") for input in inputs[(r + 2) :]
        ]
    ]

    inputs = [
        input.replace("\n", "")
        .replace("    ", "[ ]")
        .replace("   ", "[ ]")
        .replace(" ", "")
        .replace("[]", " ")
        .replace("[", "")
        .replace("]", "")
        .replace("move", "")
        .replace("from", "")
        .replace("to", "")
        for input in inputs
    ]
    stacks = [list(input) for input in inputs[:r]]

    column_stacks = []
    for i in range(len(stacks[0])):
        stack = []
        for j in range(r):
            item = stacks[j][i]
            if item != " ":
                stack.append(item)

        stack.reverse()
        column_stacks.append(stack)

    return column_stacks, instructions


def process_stacks(stacks, instructions, version=9000):
    for instruction in instructions:
        count = instruction[0]
        src = instruction[1]
        dst = instruction[2]

        if version==9000:
            for _ in range(count):
                item = stacks[src - 1].pop()
                stacks[dst - 1].append(item)
        elif version==9001:
            to_add = []
            for _ in range(count):
                item = stacks[src - 1].pop()
                to_add.append(item)
            to_add.reverse()
            for item in to_add:
                stacks[dst - 1].append(item)

