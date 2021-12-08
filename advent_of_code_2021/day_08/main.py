import display as dp


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    signal_patterns, outputs = dp.parse_inputs(inputs)

    # part 1
    easy_digits_outputs = [
        x for output in outputs for x in output if len(x) in [2, 4, 3, 7]
    ]
    print(len(easy_digits_outputs))

    # part 2
    outputs_sum = 0
    for pattern, output in zip(signal_patterns, outputs):
        output_digits = []
        signal_patterns_map = dp.map_signal_patterns(pattern)
        sorted_patterns_map = {
            dp.sort_pattern(value): key
            for (key, value) in signal_patterns_map.items()
        }
        for pattern in output:
            output_digits.append(
                str(sorted_patterns_map[dp.sort_pattern(pattern)])
            )
        outputs_sum += int(str("".join(output_digits)))

    print(outputs_sum)


if __name__ == "__main__":
    main()
