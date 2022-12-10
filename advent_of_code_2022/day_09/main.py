from rope import get_visited_tail_positions, get_visited_tail_positions_2


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    print(len(get_visited_tail_positions(inputs)))

    # part 2
    print(len(get_visited_tail_positions_2(inputs)))


if __name__ == "__main__":
    main()
