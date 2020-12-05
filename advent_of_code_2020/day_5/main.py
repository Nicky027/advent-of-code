from boarding_passes import get_seat_id, find_my_seat


def main():
    with open("input.txt", "r") as file:
        boarding_passes = file.readlines()

    print(max([get_seat_id(bp) for bp in boarding_passes]))

    print(find_my_seat(boarding_passes))


if __name__ == "__main__":
    main()
