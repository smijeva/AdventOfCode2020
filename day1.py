"""
Day 1 is simple: the task is to find two (three resp.) numbers in a list which sum adds up to 2020.
I decided to use this day to practice list comprehension for a bit.
The solution could be slightly improved by filtering the empty lists from the output product.
"""


def part1():
    file = open("input1.txt")
    entries = [int(line) for line in file]
    product = [[i * j for j in entries if i + j == 2020] for i in entries]
    print(product)


def part2():
    file = open("input1.txt")
    entries = [int(line) for line in file]
    product = [[[i * j * k for k in entries if i + j + k == 2020] for j in entries] for i in entries]
    print(product)


part2()
