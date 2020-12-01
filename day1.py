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
