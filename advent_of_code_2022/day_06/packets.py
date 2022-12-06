def get_start_of_packet_index(input: str) -> int:
    for i in range(len(input) - 3):
        sequence = input[i : (i + 4)]
        symbols = []
        unique_symbols_count = 0
        for symbol in sequence:
            if symbol not in symbols:
                symbols.append(symbol)
                unique_symbols_count += 1
        if unique_symbols_count == 4:
            return i + 4
    return 0


def get_start_of_message_index(input: str) -> int:
    for i in range(len(input) - 13):
        sequence = input[i : (i + 14)]
        symbols = []
        unique_symbols_count = 0
        for symbol in sequence:
            if symbol not in symbols:
                symbols.append(symbol)
                unique_symbols_count += 1
        if unique_symbols_count == 14:
            return i + 14
    return 0
