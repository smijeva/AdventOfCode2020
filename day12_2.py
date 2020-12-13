def rotate_left(coordinates, degree):
    for _ in range(degree):
        coordinates[0], coordinates[1] = coordinates[1], -1 * coordinates[0]
    return coordinates


def rotate_right(coordinates, degree):
    for _ in range(degree):
        coordinates[0], coordinates[1] = -1 * coordinates[1], coordinates[0]
    return coordinates


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
    waypoint_coordinates = [1, 10]

    for i in instructions:
        if i[0] in 'NSEW':
            waypoint_coordinates = step(waypoint_coordinates, i[0], i[1])
        elif i[0] == 'L':
            degree = i[1] // 90
            waypoint_coordinates = rotate_left(waypoint_coordinates, degree)
        elif i[0] == 'R':
            degree = i[1] // 90
            waypoint_coordinates = rotate_right(waypoint_coordinates, degree)
        elif i[0] == 'F':
            for _ in range(i[1]):
                coordinates = step(coordinates, 'N', waypoint_coordinates[0])
                coordinates = step(coordinates, 'E', waypoint_coordinates[1])
        else:
            raise ValueError("Unknown instruction {}".format(i[0]))

    return coordinates


def part2():
    with open("input12.txt") as file:
        instructions = [(line[0], int(line[1:])) for line in file]
    result = navigate(instructions)
    print(result)
    return result


part2()


def test_navigate():
    instructions = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
    result = navigate(instructions)
    assert result[0] == -72
    assert result[1] == 214
