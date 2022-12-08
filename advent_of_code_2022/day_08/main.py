from trees import parse_inputs, get_visible_trees, get_scenic_scores


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    print(len(get_visible_trees(parse_inputs(inputs))))

    # part 2
    print(max(get_scenic_scores(parse_inputs(inputs))))


if __name__ == "__main__":
    main()
