def parse_inputs(inputs: list) -> list:
    return [[int(x) for x in input.replace("\n", "")] for input in inputs]


def get_visible_trees(trees: list) -> list:
    nrows = len(trees)
    ncols = len(trees[0])

    visible_trees = []

    for i in range(nrows):
        for j in range(ncols):
            tree = trees[i][j]
            if (i in [0, nrows - 1]) or (j in [0, ncols - 1]):
                visible_trees.append(tree)
                continue

            same_row_trees = trees[i].copy()
            left_trees = same_row_trees[:j]
            right_trees = same_row_trees[j + 1 :]

            same_column_trees = [x[j] for x in trees].copy()
            top_trees = same_column_trees[:i]
            bottom_trees = same_column_trees[i + 1 :]

            if (
                all(list(map(lambda x: x < tree, left_trees)))
                or all(list(map(lambda x: x < tree, right_trees)))
                or all(list(map(lambda x: x < tree, top_trees)))
                or all(list(map(lambda x: x < tree, bottom_trees)))
            ):
                visible_trees.append(tree)

    return visible_trees


def get_scenic_scores(trees: list) -> list:
    nrows = len(trees)
    ncols = len(trees[0])

    scenic_scores = []

    for i in range(nrows):
        for j in range(ncols):
            tree = trees[i][j]
            if (i in [0, nrows - 1]) or (j in [0, ncols - 1]):
                scenic_scores.append(0)
                continue

            same_row_trees = trees[i].copy()
            left_trees = same_row_trees[:j]
            right_trees = same_row_trees[j + 1 :]

            same_column_trees = [x[j] for x in trees].copy()
            top_trees = same_column_trees[:i]
            bottom_trees = same_column_trees[i + 1 :]

            left_score = 0
            right_score = 0
            top_score = 0
            bottom_score = 0

            left_trees.reverse()
            for x in left_trees:
                left_score += 1
                if x >= tree:
                    break

            for x in right_trees:
                right_score += 1
                if x >= tree:
                    break

            top_trees.reverse()
            for x in top_trees:
                top_score += 1
                if x >= tree:
                    break

            for x in bottom_trees:
                bottom_score += 1
                if x >= tree:
                    break

            scenic_scores.append(
                left_score * right_score * top_score * bottom_score
            )

    return scenic_scores
