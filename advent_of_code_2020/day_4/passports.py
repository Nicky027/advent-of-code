import re
from regex import (
    four_digits,
    nine_digits,
    height_centimeters,
    height_inches,
    valid_colour,
)


def separate(inputs):
    passports = []
    passport = {}
    for i in inputs:
        if i == "\n":
            passports.append(passport)
            passport = {}
        else:
            fields = i.split(" ")
            for field in fields:
                key = field.split(":")[0]
                val = field.split(":")[1].replace("\n", "")
                passport[key] = val

    passports.append(passport)
    return passports


def validate(passport, required_fields, strict=False):
    keys = passport.keys()
    for field in required_fields:
        if field not in keys:
            return False

    if strict:
        byr = passport["byr"]
        byr_valid = (
            bool(re.match(four_digits, byr)) and 1920 <= int(byr) <= 2002
        )

        iyr = passport["iyr"]
        iyr_valid = (
            bool(re.match(four_digits, iyr)) and 2010 <= int(iyr) <= 2020
        )

        eyr = passport["eyr"]
        eyr_valid = (
            bool(re.match(four_digits, eyr)) and 2020 <= int(eyr) <= 2030
        )

        hgt = passport["hgt"]
        hgt_valid = (
            bool(re.match(height_inches, hgt)) and 59 <= int(hgt[:-2]) <= 76
        ) or (
            bool(re.match(height_centimeters, hgt))
            and 150 <= int(hgt[:-2]) <= 193
        )

        hcl = passport["hcl"]
        hcl_valid = bool(re.match(valid_colour, hcl))

        ecl = passport["ecl"]
        ecl_valid = ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        pid = passport["pid"]
        pid_valid = bool(re.match(nine_digits, pid))

        valid = (
            byr_valid
            and iyr_valid
            and eyr_valid
            and hgt_valid
            and hcl_valid
            and ecl_valid
            and pid_valid
        )

        return valid

    return True
