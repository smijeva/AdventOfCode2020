def get_2020(numbers):
    for i in range(len(numbers), 2020):
        last_num = numbers[-1]
        if last_num in numbers[:-1]:
            last_index = max(loc for loc, val in enumerate(numbers[:-1]) if val == last_num)
            new_number = len(numbers) - 1 - last_index
            numbers.append(new_number)
        else:
            numbers.append(0)

    print([i for i, x in enumerate(numbers) if x == 19])
    print([i for i, x in enumerate(numbers) if x == 0])
    print([i for i, x in enumerate(numbers) if x == 5])
    print([i for i, x in enumerate(numbers) if x == 1])
    print([i for i, x in enumerate(numbers) if x == 19])
    print([i for i, x in enumerate(numbers) if x == 13])
    print(numbers[-20:])

    return numbers[-1]


print(get_2020([19, 0, 5, 1, 10, 13]))


def test_get_2020():
    assert get_2020([0, 3, 6]) == 436
    assert get_2020([1, 3, 2]) == 1
    assert get_2020([2, 1, 3]) == 10
    assert get_2020([1, 2, 3]) == 27
    assert get_2020([2, 3, 1]) == 78
    assert get_2020([3, 2, 1]) == 438
    assert get_2020([3, 1, 2]) == 1836
