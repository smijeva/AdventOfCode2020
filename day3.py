"""
Day 3 was about counting trees in the matrix. The list comprehension solution does not seem particularly elegant this
time and it required a lot of effort to figure out why it is not working (figuring division by step_down part was
particularly difficult and I consider it un-elegant.)
"""

import math

TREES_REPEAT_PATTERN = 31
TREE = '#'


def part1(step_right, step_down):
    with open('input3.txt') as file:
        trees = [line[((i//step_down) * step_right) % TREES_REPEAT_PATTERN] == TREE and i % step_down == 0
                 for i, line in enumerate(file)]
    return sum(trees)


def part2():
    down1_trees = [part1(s, 1) for s in [1, 3, 5, 7]]
    print(down1_trees)
    print(part1(1, 2))
    print(math.prod(down1_trees) * part1(1, 2))


print(part1(3, 1))
part2()
