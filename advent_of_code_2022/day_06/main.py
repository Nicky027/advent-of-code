from packets import get_start_of_packet_index, get_start_of_message_index


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    print(get_start_of_packet_index(inputs[0].replace("\n", "")))

    # part 2
    print(get_start_of_message_index(inputs[0].replace("\n", "")))


if __name__ == "__main__":
    main()
