from initalization import parse, initialize, initialize_v2


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    print(sum(initialize(parse(inputs)).values()))
    print(sum(initialize_v2(parse(inputs)).values()))


if __name__ == "__main__":
    main()
