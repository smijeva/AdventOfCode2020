LEFT = ['E', 'N', 'W', 'S']
LEFT += LEFT

RIGHT = list(reversed(LEFT))


def step(coordinates, direction, distance):
    if direction == 'N':
        coordinates[0] += distance
    if direction == 'S':
        coordinates[0] -= distance
    if direction == 'E':
        coordinates[1] += distance
    if direction == 'W':
        coordinates[1] -= distance

    return coordinates


def navigate(instructions):
    coordinates = [0, 0]
    facing = 'E'

    for i in instructions:
        if i[0] in 'NSEW':
            coordinates = step(coordinates, i[0], i[1])
        elif i[0] == 'L':
            degree = i[1] // 90
            facing = LEFT[LEFT.index(facing) + degree]
        elif i[0] == 'R':
            degree = i[1] // 90
            facing = RIGHT[RIGHT.index(facing) + degree]
        elif i[0] == 'F':
            coordinates = step(coordinates, facing, i[1])
        else:
            raise ValueError("Unknown instruction {}".format(i[0]))

    return coordinates


def part1():
    with open("input12.txt") as file:
        instructions = [(line[0], int(line[1:])) for line in file]
    result = navigate(instructions)
    print(result)
    return result


part1()


def test_navigate():
    instructions = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
    result = navigate(instructions)
    assert result[0] == -8
    assert result[1] == 17
