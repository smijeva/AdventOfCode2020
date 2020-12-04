"""
The day 4 task is similar to day 2, but constraints on password are different. In part 1, the password must include
all mandatory fields. In part 2 these fields must also fulfill the given constraints.
"""

import re

MANDATORY_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
HAIR_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

rules = {
    'byr': lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    'iyr': lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    'eyr': lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x[:-2].isdigit() and x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193)
                     or (x[:-2].isdigit() and (x[-2:] == "in" and 59 <= int(x[:-2]) <= 79)),
    'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x) is not None,
    'ecl': lambda x: x in HAIR_COLORS,
    'pid': lambda x: re.match(r'^[0-9]{9}$', x) is not None,
    'cid': lambda _: True,
}


def load_passports(file):
    passport = {}
    for line in file:
        fields = re.findall(r'([^\s:]+):([^\s:]+)', line)
        if len(fields) == 0:
            yield passport
            passport = {}
        for f in fields:
            passport[f[0]] = f[1]
    yield passport


def is_valid1(passport):
    return all(prop in passport.keys() for prop in MANDATORY_FIELDS)


def is_valid2(passport):
    return all(rules[prop](entry) for prop, entry in passport.items())


def part1(file_name):
    with open(file_name) as file:
        return sum(is_valid1(p) for p in load_passports(file))


def part2(file_name):
    with open(file_name) as file:
        return sum(is_valid1(p) and is_valid2(p) for p in load_passports(file))


print(part2("input4.txt"))


def test_is_valid2():
    assert part2("input4_test1.txt") == 4
    assert part2("input4_test2.txt") == 0
