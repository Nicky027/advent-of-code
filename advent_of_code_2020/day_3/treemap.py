def expand_map(input_map):
    input_map["map"] = input_map["map"].apply(
        lambda x: "".join([str(x) for i in range(input_map.shape[0] * 3)])
    )
    return input_map


def traverse_map(input_map, right_steps, down_steps):
    x = 0
    y = 0
    while y < input_map.shape[0] - 1:
        x = x + right_steps
        y = y + down_steps
        if input_map.loc[y, "map"][x] == ".":
            input_map.loc[y, "map"] = (
                input_map.loc[y, "map"][:x]
                + "O"
                + input_map.loc[y, "map"][(x + 1) :]
            )
        else:
            input_map.loc[y, "map"] = (
                input_map.loc[y, "map"][:x]
                + "X"
                + input_map.loc[y, "map"][(x + 1) :]
            )

    return input_map
