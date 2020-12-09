from xmas import first_non_valid, consecutive_add_up


def main():
    with open("input.txt", "r") as file:
        input_numbers = file.readlines()

    numbers = [int(x.replace("\n", "")) for x in input_numbers]

    non_valid_number = first_non_valid(numbers, 25)
    print(non_valid_number)

    consecutive_add_up_numbers = consecutive_add_up(non_valid_number, numbers)
    print(min(consecutive_add_up_numbers) + max(consecutive_add_up_numbers))


if __name__ == "__main__":
    main()
