import math


def count_voltages_diffs(voltages):
    v = sorted(voltages)
    diffs = [0, 0, 0, 0]
    diffs[v[0]] += 1
    for i in range(1, len(v)):
        diff = v[i] - v[i - 1]
        diffs[diff] += 1

    # last adapter
    diffs[3] += 1

    return diffs


def count_voltages_combinations(voltages):
    v = sorted(voltages)
    combinations = [1]
    print(v)
    for i in range(1, len(v)):
        beginning = 0 if i - 3 < 0 else i - 3
        combinations.append(0)

        if v[i] <= 3:
            # can use the very first adapter
            combinations[i] += 1

        for offset in range(3):
            if beginning + offset == i:
                # adapter cannot be plugged into itself
                break
            if v[beginning + offset] + 3 >= v[i]:
                combinations[i] += combinations[beginning+offset]

    return combinations[-1]


def part1():
    with open("input10.txt") as file:
        voltages = [int(line) for line in file]

    diffs = count_voltages_diffs(voltages)
    result = diffs[1] * diffs[3]
    print(result)
    return result


def part2():
    with open("input10.txt") as file:
        voltages = [int(line) for line in file]

    result = count_voltages_combinations(voltages)
    print(result)
    return result


part1()
part2()


def test_count_voltages_diffs():
    t1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    t2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
          10, 3]

    diffs1 = count_voltages_diffs(t1)
    diffs2 = count_voltages_diffs(t2)

    assert diffs1[1] == 7
    assert diffs1[3] == 5

    assert diffs2[1] == 22
    assert diffs2[3] == 10


def test_count_voltages_combinations():
    t1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    t2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
          10, 3]

    comb1 = count_voltages_combinations(t1)
    comb2 = count_voltages_combinations(t2)

    assert comb1 == 8
    assert comb2 == 19208
