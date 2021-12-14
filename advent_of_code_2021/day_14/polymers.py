from collections import Counter


def parse_inputs(inputs):
    polymer = list(inputs[0])
    rules = {}
    for input in inputs[2:]:
        input_parts = input.split(" -> ")
        rules[input_parts[0]] = input_parts[1]
    return polymer, rules


def step(polymer, rules):
    new_polymer = []
    for i, element in enumerate(polymer):
        new_polymer.append(element)
        pair = "".join(polymer[i : i + 2])
        insertion = rules.get(pair)
        if insertion:
            new_polymer.append(insertion)
    return new_polymer


def score(polymer):
    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())


def smart_polymer_representation(polymer, rules):
    pairs = {rule: 0 for rule in rules.keys()}
    for i in range(len(polymer) - 1):
        pair = "".join(polymer[i : i + 2])
        if pair:
            pairs[pair] += 1
    return pairs


def smart_rules_representation(rules):
    smart_rules = {}
    for pair, element in rules.items():
        smart_rules[pair] = ["".join([pair[0], element]), "".join([element, pair[1]])]
    return smart_rules


def smart_step(polymer, rules):
    new_polymer = polymer.copy()
    for pair, count in polymer.items():
        new_pairs = rules[pair]
        new_polymer[new_pairs[0]] += count
        new_polymer[new_pairs[1]] += count
        new_polymer[pair] -= count
    return new_polymer


def smart_score(polymer):
    elements = set(y for x in polymer.keys() for y in list(x))

    counts = {element: 0 for element in elements}
    for pair, count in polymer.items():
        counts[pair[0]] += count
        counts[pair[1]] += count

    scores = {element: 0 for element in elements}
    for element, count in counts.items():
        if count % 2 == 0:
            scores[element] = int(count / 2)
        else:
            scores[element] = int((count - 1) / 2 + 1)

    return max(scores.values()) - min(scores.values())
