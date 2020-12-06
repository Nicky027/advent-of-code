from functools import reduce


def split_groups(input_array):
    output_array = []
    group = []
    for entry in input_array:
        if entry == "\n":
            new_group = group.copy()
            output_array.append(new_group)
            group = []
        else:
            group.append(entry.replace("\n", ""))

    new_group = group.copy()
    output_array.append(new_group)

    return output_array


def count_distinct(group, reduce_function):
    return len(
        reduce(
            reduce_function,
            [{q for q in questions} for questions in group],
        )
    )
