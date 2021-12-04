import numpy as np


def parse_inputs(inputs):
    drawn_numbers = np.array(parse_line(inputs[0]))
    boards = []
    board = []
    for i in range(2, len(inputs)):
        if inputs[i] == "":
            boards.append(np.array(board))
            board = []
        else:
            board.append(parse_line(inputs[i], sep=" "))
    boards.append(np.array(board))

    return drawn_numbers, boards


def parse_line(line, sep=","):
    return [int(x.strip()) for x in line.split(sep) if x.strip() != ""]


def get_board_winning_round(board, drawn_numbers):
    for i in range(5, drawn_numbers.shape[0]):
        rows = np.apply_along_axis(
            lambda x: check_line(x, drawn_numbers[0:i]), axis=1, arr=board
        )
        if rows.any():
            return i

        columns = np.apply_along_axis(
            lambda x: check_line(x, drawn_numbers[0:i]), axis=0, arr=board
        )
        if columns.any():
            return i

    return np.Inf


def check_line(line, drawn_numbers):
    return np.intersect1d(line, drawn_numbers).shape[0] == line.shape[0]


def score_winning_board(winning_board, drawn_numbers):
    undrawn_numbers = np.setdiff1d(winning_board.ravel(), drawn_numbers)
    return np.sum(undrawn_numbers) * drawn_numbers[-1]
