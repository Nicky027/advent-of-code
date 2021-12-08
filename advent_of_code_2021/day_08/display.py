def parse_inputs(inputs):
    signal_patterns = []
    outputs = []
    for input in inputs:
        split_input = input.split(" | ")
        signal_patterns.append(split_input[0].split(" "))
        outputs.append(split_input[1].split(" "))
    return signal_patterns, outputs


def map_signal_patterns(pattern_list):
    signal_patterns_map = {}
    zero_six_nine = []
    two_three_five = []
    for pattern in pattern_list:
        value = pattern
        length = len(pattern)
        if length in [2, 4, 3, 7]:
            if length == 2:
                key = 1
            elif length == 4:
                key = 4
            elif length == 3:
                key = 7
            elif length == 7:
                key = 8
            signal_patterns_map[key] = value
        elif length == 6:
            zero_six_nine.append(value)
        elif length == 5:
            two_three_five.append(value)

    for pattern in zero_six_nine:
        has_both_1_segments = True
        has_all_4_segments = True

        for segment in signal_patterns_map[4]:
            if segment not in pattern:
                has_all_4_segments = False

        for segment in signal_patterns_map[1]:
            if segment not in pattern:
                has_both_1_segments = False

        if has_both_1_segments:
            if has_all_4_segments:
                signal_patterns_map[9] = pattern
            else:
                signal_patterns_map[0] = pattern
        else:
            signal_patterns_map[6] = pattern

    for pattern in two_three_five:
        if (
            signal_patterns_map[1][0] in pattern
            and signal_patterns_map[1][1] in pattern
        ):
            signal_patterns_map[3] = pattern
        else:
            for segment in pattern:
                if segment not in string_to_list(signal_patterns_map[6]):
                    signal_patterns_map[2] = pattern
        if pattern != signal_patterns_map.get(
            2
        ) and pattern != signal_patterns_map.get(3):
            signal_patterns_map[5] = pattern

    return signal_patterns_map


def string_to_list(input_string):
    return [x for x in input_string]


def sort_pattern(pattern):
    l = string_to_list(pattern)
    list.sort(l)
    return "".join(l)
