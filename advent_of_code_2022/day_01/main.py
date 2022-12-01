from calories import get_sums


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    sums = get_sums(inputs)
    print(max(sums))

    # part 2
    sums.sort(reverse=True)
    print(sum(sums[0:3]))


if __name__ == "__main__":
    main()
