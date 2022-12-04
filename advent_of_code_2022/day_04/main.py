from cleaning import count_fully_contained_pairs, count_overlapping_pairs


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    pairs = [input.replace("\n", "") for input in inputs]

    # part 1
    print(count_fully_contained_pairs(pairs))

    # part 2
    print(count_overlapping_pairs(pairs))


if __name__ == "__main__":
    main()
