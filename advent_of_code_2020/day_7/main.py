from bags import parse_rules, contains, count_nested_bags


def main():
    with open("input.txt", "r") as file:
        rules_list = file.readlines()

    rules = parse_rules(rules_list)

    print(sum(map(lambda x: contains(x, "shiny gold", rules), rules)))
    print(count_nested_bags("shiny gold", rules))


if __name__ == "__main__":
    main()
