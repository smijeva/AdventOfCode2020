arrival = 1000655
buses = [17, 37, 571, 13, 23, 29, 401, 41, 19]
x = 0
buses2 = [17, x, x, x, x, x, x, x, x, x, x, 37, x, x, x, x, x, 571, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
          13, x, x, x, x, 23, x, x, x, x, x, 29, x, 401, x, x, x, x, x, x, x, x, x, 41, x, x, x, x, x, x, x, x, 19]


def find_bus():
    departure = arrival
    while True:
        for b in buses:
            if departure % b == 0:
                return b, departure
        departure += 1


def find_bus_sequence(schedule, beginning):
    departure = beginning
    while True:
        for i, b in enumerate(schedule):
            if b == x:
                continue
            if (departure + i) % b != 0:
                break
            if i == (len(schedule) - 1):
                return departure
        departure += 1


result = find_bus_sequence(buses2, 100000000000000)
print(result)


def test_find_bus_sequence():
    schedule = [7, 13, x, x, 59, x, 31, 19]
    r = find_bus_sequence(schedule, 1068780)
    assert r == 1068781
