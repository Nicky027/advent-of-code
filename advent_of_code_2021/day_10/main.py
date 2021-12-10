import syntax as s


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    errors, completions = s.find_errors_and_completions(inputs)

    # part 1
    print(s.score_errors(errors))

    # part 2
    print(s.score_completions(completions))


if __name__ == "__main__":
    main()
