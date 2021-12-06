import lanternfish as lf


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    lanternfish = [int(x) for input in inputs for x in input.split(",")]

    # part 1
    for i in range(80):
        lf.day_pass(lanternfish)
    print(len(lanternfish))

    # part 2
    lanternfish = [int(x) for input in inputs for x in input.split(",")]
    lanternfish_map = lf.fish_counter(lanternfish)
    for i in range(256):
        lanternfish_map = lf.smart_day_pass(lanternfish_map)
    print(sum(lanternfish_map.values()))


if __name__ == "__main__":
    main()
