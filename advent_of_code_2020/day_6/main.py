from groups import split_groups, count_distinct


def main():
    with open("input.txt", "r") as file:
        questions = file.readlines()

    groups = split_groups(questions)

    print(
        sum(
            [
                count_distinct(group, lambda a, b: a.union(b))
                for group in groups
            ]
        )
    )
    print(
        sum(
            [
                count_distinct(group, lambda a, b: a.intersection(b))
                for group in groups
            ]
        )
    )


if __name__ == "__main__":
    main()
