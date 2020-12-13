import copy

FREE = "L"
FLOOR = "."
OCCUPIED = "#"


def is_place_occupied(x, y, matrix):
    if x < 0 or x >= len(matrix):
        return False
    if y < 0 or y >= len(matrix[0]):
        return False
    if matrix[x][y] == OCCUPIED:
        return True
    return False


def neighbors_occupied(x, y, matrix):
    neighbors = [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1),
                 (x, y + 1), (x, y - 1),
                 (x - 1, y + 1), (x - 1, y), (x - 1, y - 1)]

    return sum(is_place_occupied(i, j, matrix) for i, j in neighbors)


def is_direction_occupied(x, y, i, j, matrix):
    x += i
    y += j
    while len(matrix) > x > -1 and len(matrix[0]) > y > -1:
        if matrix[x][y] == OCCUPIED:
            return True
        if matrix[x][y] == FREE:
            return False
        x += i
        y += j
    return False


def neighbors_occupied2(x, y, matrix):
    directions = [(+1, +1), (+1, 0), (+1, -1),
                  (0, +1), (0, -1),
                  (-1, +1), (-1, 0), (-1, -1)]

    return sum(is_direction_occupied(x, y, i, j, matrix) for i, j in directions)


def make_step(matrix):
    new_matrix = copy.deepcopy(matrix)
    has_changed = False
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == FREE and neighbors_occupied(x, y, matrix) == 0:
                new_matrix[x][y] = OCCUPIED
                has_changed = True
            if matrix[x][y] == OCCUPIED and neighbors_occupied(x, y, matrix) >= 4:
                new_matrix[x][y] = FREE
                has_changed = True

    return new_matrix, has_changed


def make_step2(matrix):
    new_matrix = copy.deepcopy(matrix)
    has_changed = False
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == FREE and neighbors_occupied2(x, y, matrix) == 0:
                new_matrix[x][y] = OCCUPIED
                has_changed = True
            if matrix[x][y] == OCCUPIED and neighbors_occupied2(x, y, matrix) >= 5:
                new_matrix[x][y] = FREE
                has_changed = True

    return new_matrix, has_changed


def part1():
    with open("input11.txt") as file:
        matrix = [list(x) for x in file.read().split("\n")]

    while True:
        new_matrix, has_changed = make_step(matrix)
        if not has_changed:
            break
        matrix = new_matrix

    result = sum(sum(y == OCCUPIED for y in x) for x in matrix)
    print(result)

    return result


def part2(file_name):
    with open(file_name) as file:
        matrix = [list(x) for x in file.read().split("\n")]

    while True:
        new_matrix, has_changed = make_step2(matrix)
        if not has_changed:
            break
        matrix = new_matrix

    result = sum(sum(y == OCCUPIED for y in x) for x in matrix)
    print(result)

    return result


# part1()
part2("input11.txt")


def test_part2():
    assert part2("input11_test1.txt") == 26
