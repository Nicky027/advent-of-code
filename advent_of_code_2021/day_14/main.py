import polymers as ps


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    inputs = [input.replace("\n", "") for input in inputs]

    polymer, rules = ps.parse_inputs(inputs)
    smart_polymer = ps.smart_polymer_representation(polymer, rules)
    smart_rules = ps.smart_rules_representation(rules)

    # part 1
    for _ in range(10):
        polymer = ps.step(polymer, rules)
    print(ps.score(polymer))

    # part 2
    for _ in range(40):
        smart_polymer = ps.smart_step(smart_polymer, smart_rules)
    print(ps.smart_score(smart_polymer))


if __name__ == "__main__":
    main()
