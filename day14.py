import re


def is_kth_bit_set(n, k):
    if (n >> k) & 1:
        return True
    return False


def apply_mask1(value, mask):
    zeroes = []
    ones = []
    for i, x in enumerate(reversed(mask)):
        if x == '1':
            ones.append(i)
        if x == '0':
            zeroes.append(i)

    for i in zeroes:
        if is_kth_bit_set(value, i):
            value -= 2**i

    for i in ones:
        if not is_kth_bit_set(value, i):
            value += 2**i

    return value


def apply_mask2(value, mask):
    xses = []
    ones = []

    for i, x in enumerate(reversed(mask)):
        if x == '1':
            ones.append(i)
        if x == 'X':
            xses.append(i)

    for i in ones:
        if not is_kth_bit_set(value, i):
            value += 2**i

    values = [value]

    for i in xses:
        new_values = []
        if is_kth_bit_set(value, i):
            for v in values:
                # Add values without bit
                new_values.append(v - 2 ** i)
        else:
            for v in values:
                # Add values with bit
                new_values.append(v + 2 ** i)
        values += new_values

    return values


def part1():
    current_mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    data = {}
    with open("input14.txt") as file:
        for line in file:
            if line.startswith("mask"):
                current_mask = line[7:-1]
            elif line.startswith("mem"):
                match = re.search(r'^mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)$', line)
                value = apply_mask1(int(match["value"]), current_mask)
                data[match["address"]] = value

    print(sum(data.values()))


def part2():
    current_mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    data = {}
    with open("input14.txt") as file:
        for line in file:
            if line.startswith("mask"):
                current_mask = line[7:-1]
            elif line.startswith("mem"):
                match = re.search(r'^mem\[(?P<address>[0-9]+)\] = (?P<value>[0-9]+)$', line)
                addresses = apply_mask2(int(match["address"]), current_mask)
                for a in addresses:
                    data[a] = int(match["value"])

    print(sum(data.values()))


part1()
part2()
