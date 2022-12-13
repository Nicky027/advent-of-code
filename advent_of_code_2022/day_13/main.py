from packets import parse_inputs, get_right_pair_indices, sort_packets


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    pairs = parse_inputs(inputs)
    # for i, pair in enumerate(pairs, 1):
    #     print(f"Pair {i}")
    #     print(pair[0])
    #     print(pair[1])
    #     print("\n")

    right_pairs_indices = get_right_pair_indices(pairs)
    print(sum(right_pairs_indices))

    # part 2
    all_packets = [packet for pair in pairs for packet in pair]
    all_packets.append([[2]])
    all_packets.append([[6]])
    sort_packets(all_packets)
    first_divider_packet_index = all_packets.index([[2]]) + 1
    second_divider_packet_index = all_packets.index([[6]]) + 1
    print(first_divider_packet_index * second_divider_packet_index)


if __name__ == "__main__":
    main()
