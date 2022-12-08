from directory import parse_inputs, get_size_of_directory, print_directory


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    files, directories = parse_inputs(inputs)
    distinct_directories = set(files.keys()).union(set(directories.keys()))
    directory_sizes = [
        get_size_of_directory(directory, files, directories)
        for directory in distinct_directories
    ]

    # part 1
    print(sum([x for x in directory_sizes if x <= 100000]))

    # part 2
    total_used_space = get_size_of_directory("/", files, directories)
    free_space = 70000000 - total_used_space
    required_additional_space = 30000000 - free_space
    print(min([x for x in directory_sizes if x >= required_additional_space]))


if __name__ == "__main__":
    main()
