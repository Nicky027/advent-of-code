from passports import separate, validate


def main():
    with open("input.txt", "r") as file:
        inputs = file.readlines()

    passports = separate(inputs)
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    print(sum([validate(passport, required_fields) for passport in passports]))

    print(
        sum(
            [
                validate(passport, required_fields, strict=True)
                for passport in passports
            ]
        )
    )


if __name__ == "__main__":
    main()
