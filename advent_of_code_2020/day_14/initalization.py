from itertools import product


def parse(inputs):
    parsed = []
    for line in inputs:
        split = line.split(" = ")
        if split[0] == "mask":
            parsed.append([split[0], split[1].replace("\n", "")])
        else:
            address = int(
                bin(int(split[0].replace("mem[", "").replace("]", "")))[2:]
            )
            number = int(bin(int(split[1].replace("\n", "")))[2:])
            parsed.append([f"{address:036d}", f"{number:036d}"])
    return parsed


def apply_value_mask(value, mask):
    new_value_digits = []
    for index, digit in enumerate(mask):
        if digit == "X":
            new_value_digits.append(value[index])
        else:
            new_value_digits.append(digit)
    return "".join(new_value_digits)


def initialize(inputs):
    mask = "".join("X" for i in range(36))
    memory = {}
    for line in inputs:
        if line[0] == "mask":
            mask = line[1]
        else:
            memory[line[0]] = int(apply_value_mask(line[1], mask), 2)
    return memory


def apply_address_mask(address, mask):
    new_address_digits = []
    for index, digit in enumerate(mask):
        if digit == "0":
            new_address_digits.append(address[index])
        else:
            new_address_digits.append(digit)
    return "".join(new_address_digits)


def get_all_addresses(address):
    addresses = []
    floating_bits = list(
        filter(lambda x: x[1] == "X", enumerate(list(address)))
    )
    possibilities = list(product([0, 1], repeat=len(floating_bits)))
    for possibility in possibilities:
        possible_address = list(address)
        i = 0
        for index, _ in floating_bits:
            possible_address[index] = str(possibility[i])
            i += 1
        addresses.append("".join(possible_address))
    return addresses


def initialize_v2(inputs):
    mask = "".join("X" for i in range(36))
    memory = {}
    for line in inputs:
        if line[0] == "mask":
            mask = line[1]
        else:
            addresses = get_all_addresses(apply_address_mask(line[0], mask))
            for address in addresses:
                memory[address] = int(line[1], 2)
    return memory
