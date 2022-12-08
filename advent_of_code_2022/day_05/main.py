from crates import parse_inputs, process_stacks


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    rows = 8
    stacks, instructions = parse_inputs(inputs, rows)
    stacks_2, _ = parse_inputs(inputs, rows)

    # part 1
    process_stacks(stacks, instructions, version=9000)
    print("".join([stack[-1] for stack in stacks]))

    # part 2
    process_stacks(stacks_2, instructions, version=9001)
    print("".join([stack[-1] for stack in stacks_2]))


if __name__ == "__main__":
    main()
