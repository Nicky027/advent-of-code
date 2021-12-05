import lines as l


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    # part 1
    lines = l.get_lines(inputs)
    point_crossings = l.get_point_crossings(lines)
    print(len(list(filter(lambda x: x > 1, point_crossings.values()))))

    # part 2
    lines_2 = l.get_lines(inputs, diagonals=True)
    point_crossings_2 = l.get_point_crossings(lines_2)
    print(len(list(filter(lambda x: x > 1, point_crossings_2.values()))))


if __name__ == "__main__":
    main()
