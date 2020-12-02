def validator_1(p):
    policy = p.split(":")[0]
    password = p.split(":")[1][1:]

    policy_letter = policy.split(" ")[1]
    policy_letter_min = int(policy.split(" ")[0].split("-")[0])
    policy_letter_max = int(policy.split(" ")[0].split("-")[1])

    letter_count = password.count(policy_letter)
    valid = policy_letter_min <= letter_count <= policy_letter_max

    return valid


def validator_2(p):
    policy = p.split(":")[0]
    password = p.split(":")[1][1:]

    policy_letter = policy.split(" ")[1]
    policy_letter_min = int(policy.split(" ")[0].split("-")[0])
    policy_letter_max = int(policy.split(" ")[0].split("-")[1])

    valid = (password[policy_letter_min-1] == policy_letter) ^ (password[policy_letter_max-1] == policy_letter)

    return valid


def input_validator(input_df, validator):
    input_df["valid"] = input_df["policy_password"].apply(validator)
    return input_df["valid"].sum()