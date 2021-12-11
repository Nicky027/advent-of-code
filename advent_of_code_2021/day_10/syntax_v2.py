def find_errors_and_completions(inputs):
    errors = []
    completions = []
    for input in inputs:
        error = find_error(input)
        if error:
            errors.append(error)
        else:
            completions.append(find_completion(input))
    return errors, completions


def find_error(input):
    open_brackets = []
    for x in input:
        if x in ["(", "[", "{", "<"]:
            open_brackets.append(x)
        else:
            y = open_brackets.pop()
            if close_bracket(y) != x:
                return x


def find_completion(input):
    open_brackets = []
    for x in input:
        if x in ["(", "[", "{", "<"]:
            open_brackets.append(x)
        else:
            open_brackets.pop()
    open_brackets.reverse()
    return [close_bracket(x) for x in open_brackets]


def score_errors(errors):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return sum(scores[error] for error in errors)


def score_completions(completions):
    scores = [score_completion(c) for c in completions]
    scores.sort()
    return scores[int(len(scores) / 2)]


def score_completion(completion):
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for x in completion:
        score = score * 5 + scores[x]
    return score


def close_bracket(opened_bracket):
    return {"(": ")", "{": "}", "[": "]", "<": ">"}[opened_bracket]


def open_bracket(closed_bracket):
    return {")": "(", "}": "{", "]": "[", ">": "<"}[closed_bracket]
