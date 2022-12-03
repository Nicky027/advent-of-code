from score import get_total_score


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    games = [input.replace("\n", "").split(" ") for input in inputs]

    # part 1
    print(get_total_score(games))

    # part 2
    print(get_total_score(games, part=2))


if __name__ == "__main__":
    main()
