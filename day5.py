"""Day 5 was about searching binary space partitioning and a lot about off by one error."""

def parse_place(partitions):
    low_ix = 0
    high_ix = 127
    for c in partitions[:7]:
        if c == "F":
            high_ix = low_ix + ((high_ix - low_ix) // 2)
        elif c == "B":
            low_ix = high_ix - ((high_ix - low_ix) // 2)
        else:
            raise "Unexpected position : " + c + " expected F (front) or B (back)"
    row = high_ix
    low_ix = 0
    high_ix = 7
    for c in partitions[7:10]:
        if c == "L":
            high_ix = low_ix + ((high_ix - low_ix) // 2)
        elif c == "R":
            low_ix = high_ix - ((high_ix - low_ix) // 2)
        else:
            raise "Unexpected position : " + c + " expected L (left) or R (right)"
    col = low_ix
    return (row * 8) + col


def part1():
    with open("input5.txt") as file:
        m = max(parse_place(line) for line in file)
        print(m)


def part2():
    with open("input5.txt") as file:
        seats = [parse_place(line) for line in file]
        all_seats = range(0, max(seats) + 1)
        free = set(all_seats) - set(seats)
        print(sorted(free))


part2()


def test_parse_place():
    assert parse_place("FBFBBFFRLR") == 357
    assert parse_place("FFFBBBFRRR") == 119
    assert parse_place("BBFFBBFRLL") == 820
    assert parse_place("BFFFBBFRRR") == 567
