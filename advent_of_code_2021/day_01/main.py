from counter import count_increasing


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [int(input) for input in inputs]

    # part 1
    print(count_increasing(inputs))

    # part 2
    window_sums = []
    for i in range(len(inputs) - 2):
        window_sums.append(sum(inputs[i : i + 3]))
    print(count_increasing(window_sums))


if __name__ == "__main__":
    main()
