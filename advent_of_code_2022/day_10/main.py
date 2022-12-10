from processor import get_registry_values, get_signal_strengths, crt_render


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    # part 1
    registry_values = get_registry_values(inputs)
    signal_strengths = get_signal_strengths(
        registry_values, cycles=[20, 60, 100, 140, 180, 220]
    )
    print(sum(signal_strengths))

    # part 2
    crt_render(registry_values)


if __name__ == "__main__":
    main()
