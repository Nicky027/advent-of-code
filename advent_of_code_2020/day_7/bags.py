def parse_rules(rules_list):
    rules = {}

    for rule in rules_list:
        rule_key = rule.split(" contain ")[0].replace(" bags", "")
        rule_values = rule.split(" contain ")[1].split(", ")
        rules[rule_key] = [
            (
                int(" ".join(value.split(" ")[:1]).replace("no", "0")),
                " ".join(value.split(" ")[1:3])
                .replace("\n", "")
                .replace(".", ""),
            )
            for value in rule_values
        ]

    return rules


def contains(bag_1, bag_2, rules):
    """Returns True if bag_1 contains bag_2 and False otherwise"""

    if rules[bag_1] == [(0, "other bags")]:
        return False
    elif bag_2 in [x[1] for x in rules[bag_1]]:
        return True
    else:
        return any(
            map(
                lambda x: contains(x, bag_2, rules),
                [x[1] for x in rules[bag_1]],
            )
        )


def count_nested_bags(bag, rules):
    if bag == "other bags":
        return 0
    else:
        nested_bags = rules[bag]
        return sum(
            map(
                lambda x: x[0] * (1 + count_nested_bags(x[1], rules)),
                nested_bags,
            )
        )
