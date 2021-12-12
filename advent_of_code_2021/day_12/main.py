import caves as cv
from tqdm import tqdm


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    caves = cv.parse_inputs(inputs)

    # part 1
    paths = [["start"]]
    previous_paths = 0
    while previous_paths != len(paths):
        previous_paths = len(paths)
        cv.find_paths(caves, paths, part=1)
    print(len(cv.clean_paths(paths)))

    # part 2
    paths = [["start"]]
    previous_paths = 0
    while previous_paths != len(paths):
        previous_paths = len(paths)
        cv.find_paths(caves, paths, part=2)

    print(len(cv.clean_paths(paths, part=2)))


if __name__ == "__main__":
    main()
