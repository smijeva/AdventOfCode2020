def find_invalid_number(numbers, preamble_length):
    buffer = numbers[:preamble_length]
    for n in numbers[preamble_length:]:
        is_ok = False
        for i_ix, i in enumerate(buffer):
            for j_ix, j in enumerate(buffer):
                if i + j == n and i_ix != j_ix:
                    is_ok = True
                    break
            if is_ok:
                break
        if not is_ok:
            return n
        buffer.pop(0)
        buffer.append(n)


def find_sum(numbers, wanted_sum):
    pointer_low = 0
    for pointer_high in range(1, len(numbers)):
        result = sum(numbers[pointer_low:pointer_high])
        if result == wanted_sum and pointer_low != pointer_high:
            return min(numbers[pointer_low:pointer_high]) + max(numbers[pointer_low:pointer_high])
        while result > wanted_sum:
            pointer_low += 1
            result = sum(numbers[pointer_low:pointer_high])
            if result == wanted_sum and pointer_low != pointer_high:
                return min(numbers[pointer_low:pointer_high]) + max(numbers[pointer_low:pointer_high])
    return -1


def part1():
    with open("input9.txt") as file:
        numbers = [int(line) for line in file]
    result = find_invalid_number(numbers, 25)
    print(result)
    return result


def part2(wanted_sum):
    with open("input9.txt") as file:
        numbers = [int(line) for line in file]
    print(find_sum(numbers, wanted_sum))


part2(part1())


def test_find_invalid_number():
    numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    result = find_invalid_number(numbers, 5)
    assert result == 127


def test_find_sum():
    numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    result = find_sum(numbers, 127)
    assert result == 62


