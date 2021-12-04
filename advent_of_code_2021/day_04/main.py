import bingo as bg
import numpy as np


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    drawn_numbers, boards = bg.parse_inputs(inputs)

    # part 1
    winning_board = None
    winning_round = np.Inf

    # part 2
    last_winning_board = None
    last_winning_round = 0

    for board in boards:
        # part 1
        wr = bg.get_board_winning_round(board, drawn_numbers)
        if wr < winning_round:
            winning_round = wr
            winning_board = board

        # part 2
        if wr > last_winning_round:
            last_winning_round = wr
            last_winning_board = board

    # part 1
    print(
        bg.score_winning_board(winning_board, drawn_numbers[0:winning_round])
    )

    # part 2
    print(
        bg.score_winning_board(
            last_winning_board, drawn_numbers[0:last_winning_round]
        )
    )


if __name__ == "__main__":
    main()
