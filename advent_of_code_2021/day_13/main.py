import origami as og
import numpy as np
np.set_printoptions(threshold=2000, linewidth=200)

def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]
    dots, fold_lines = og.parse_inputs(inputs)

    # part 1
    dots = og.fold(dots, fold_lines[0])
    print(len(dots))

    # part 2
    for line in fold_lines[1:]:
        dots = og.fold(dots, line)
    print(og.dots_to_code(dots))

if __name__ == "__main__":
    main()
