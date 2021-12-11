import syntax as s
import syntax_v2 as s2


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    # version 1
    errors, completions = s.find_errors_and_completions(inputs)
    # part 1
    print(s.score_errors(errors))
    # part 2
    print(s.score_completions(completions))

    # version 2
    errors, completions = s2.find_errors_and_completions(inputs)
    # part 1
    print(s2.score_errors(errors))
    # part 2
    print(s2.score_completions(completions))


if __name__ == "__main__":
    main()
