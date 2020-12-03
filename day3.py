import math

TREES_REPEAT_PATTERN = 31
TREE = '#'


def part1(step_right, step_down):
    with open('input3.txt') as file:
        trees = [line[(i * step_right) % TREES_REPEAT_PATTERN] == TREE
                 for i, line in enumerate(file)
                 if i % step_down == 0]
    return sum(trees)


def part2():
    down1_trees = [part1(s, 1) for s in [1, 3, 5, 7]]
    print(down1_trees)
    print(part1(1, 2))
    print(math.prod(down1_trees) * part1(1, 2))


print(part1(3, 1))
part2()
