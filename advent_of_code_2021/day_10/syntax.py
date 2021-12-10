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
    for i, x in enumerate(input):
        if x in ["(", "[", "{", "<"]:
            continue
        else:
            y = find_closest_single_open_bracket(i, input)
            if y is not None and close_bracket(y) != x:
                return x


def find_closest_single_open_bracket(i, input):
    j = i - 1
    closed_bracket_counts = {x: 0 for x in [")", "]", "}", ">"]}
    while j > 0:
        x = input[j]
        if x in [")", "]", "}", ">"]:
            closed_bracket_counts[x] += 1
        else:
            y = close_bracket(x)
            if closed_bracket_counts[y] == 0:
                return x
            else:
                closed_bracket_counts[y] -= 1
        j -= 1


def find_completion(input):
    open_brackets = []
    for x in input:
        if x in ["(", "[", "{", "<"]:
            open_brackets.append(x)
        else:
            remove_last(open_bracket(x), open_brackets)
    open_brackets.reverse()
    return [close_bracket(x) for x in open_brackets]


def remove_last(x, open_brackets):
    open_brackets.reverse()
    open_brackets.remove(x)
    open_brackets.reverse()


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
