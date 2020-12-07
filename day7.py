"""
Day 7 was finally about some graph-oriented problem. There was a set of rules about bags: how many bags must the said
bag include. In the first part, it was needed to backtrack how many types of bag can (transitively) include the bag.
I used a reversed set of rules for this, with basic reachability algo (based on DFS). The second part was about counting
bags inside a bag, easy to do with a bit of recursion.
"""

import re


BAG_NAME = 'shiny gold bag'


def load_rules(file_name):
    with open(file_name) as file:
        content = file.read()

    sentences = content.split(".\n")
    rules = {}
    for s in sentences:
        parts = s.split(" contain ")
        bag = parts[0].rstrip("s")

        if parts[1] == "no other bags":
            rules[bag] = []
            continue

        content_bags = re.findall(r'([0-9]+) ([^,]+ bag)', parts[1])
        rules[bag] = [(cb[1], int(cb[0])) for cb in content_bags]

    return rules


def load_reversed_rules(file_name):
    with open(file_name) as file:
        content = file.read()

    sentences = content.split(".\n")
    reversed_rules = {}
    for s in sentences:
        parts = s.split(" contain ")
        bag = parts[0].rstrip("s")
        if bag not in reversed_rules.keys():
            reversed_rules[bag] = []

        content_bags = re.findall(r'([0-9]+) ([^,]+ bag)', parts[1])
        for cb in content_bags:
            if cb[1] in reversed_rules.keys():
                reversed_rules[cb[1]].append(bag)
            else:
                reversed_rules[cb[1]] = [bag]

    return reversed_rules


def part1(file_name):
    reversed_rules = load_reversed_rules(file_name)
    to_visit = reversed_rules[BAG_NAME]
    seen = set()
    while len(to_visit) > 0:
        current = to_visit.pop()
        if current in seen:
            continue
        seen.add(current)
        to_visit.extend(reversed_rules[current])
    print(len(seen))
    return len(seen)


def count_bags_inside(rules, bag_name):
    """
    Returns number of bags in the bag INCLUDING the given bag.
    :param rules: A dictionary mapping bag to tuple (bag_it_must_contain, count of these bags)
    :param bag_name: Name of a bag for which the count of included bags is computed.
    """
    total_count = 1
    for bag, count in rules[bag_name]:
        total_count += count * count_bags_inside(rules, bag)
    return total_count


def part2(file_name):
    rules = load_rules(file_name)
    result = count_bags_inside(rules, BAG_NAME) - 1
    print(result)
    return result


part1('input7.txt')
part2('input7.txt')


def test_load_rules():
    r = load_rules("input7_test1.txt")
    assert len(r) == 9


def test_part1():
    r = part1("input7_test1.txt")
    assert r == 4


def test_part2():
    r = part2("input7_test1.txt")
    assert r == 32

    r = part2("input7_test2.txt")
    assert r == 126
