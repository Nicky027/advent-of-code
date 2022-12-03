from typing import List

scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}


def get_score_part_1(game: List) -> int:
    score = scores[game[1]]

    if scores[game[0]] == scores[game[1]]:
        score += 3

    if (
        (game[0] == "A" and game[1] == "Y")
        or (game[0] == "B" and game[1] == "Z")
        or (game[0] == "C" and game[1] == "X")
    ):
        score += 6

    return score


def get_score_part_2(game: List) -> int:
    score = 0
    if game[1] == "Y":
        score = score + scores[game[0]] + 3
    elif game[1] == "X":
        if game[0] == "A":
            score += 3
        elif game[0] == "B":
            score += 1
        else:
            score += 2
    else:
        score += 6
        if game[0] == "A":
            score += 2
        elif game[0] == "B":
            score += 3
        else:
            score += 1

    return score


def get_total_score(games: List, part=1) -> int:
    score = 0
    for game in games:
        score += (
            get_score_part_1(game) if part == 1 else get_score_part_2(game)
        )
    return score
