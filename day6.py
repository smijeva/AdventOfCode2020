def part1():
    with open('input6.txt') as file:
        content = file.read()

    groups = content.split("\n\n")
    group_answers = [set.union(*[set(line) for line in g.split("\n")]) for g in groups]
    print(sum(len(a) for a in group_answers))


def part2():
    with open('input6.txt') as file:
        content = file.read()

    groups = content.split("\n\n")
    group_answers = [set.intersection(*[set(line) for line in g.split("\n")]) for g in groups]
    print(sum(len(a) for a in group_answers))


part2()
