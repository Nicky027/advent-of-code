from steering import update_position


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    # part 1
    x, y = update_position(x=0, y=0, commands=inputs, steering_method="Part 1")
    print(x, y, x * y)

    # part 2
    x, y = update_position(
        x=0, y=0, aim=0, commands=inputs, steering_method="Part 2"
    )


if __name__ == "__main__":
    main()
