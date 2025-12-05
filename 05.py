Range = tuple[int, int]

def load_input(test: bool = False) -> (list[Range], list[int]):
    with open(f"inputs/05{'-test' if test else ''}.txt", "r") as f:
        ranges, numbers = f.read().split("\n\n")

    # I'll process numbers now, maybe it is not optimal
    # because it's another iteration but cleaner to work with

    ranges = [
        (int(start), int(end))
        for line in ranges.splitlines()
        for start, end in [line.split("-")]
    ]

    numbers = [int(n) for n in numbers.splitlines()]

    return ranges, numbers


def part1(input: [list[Range], list[int]]) -> int:
    ranges, numbers = input

    counter = 0
    for n in numbers:
        for s, e in ranges:
            if s <= n <= e:
                # print(f"{n} is fresh in range: {s} - {e}")
                counter += 1
                break

    return counter


def part2(input: list[list[Range], list[int]]) -> int:
    uranges, _numbers = input

    # sort by start, then I can assume that no following start would beat my current start
    ranges = sorted(uranges, key=lambda r: r[0])

    counter = 0
    index = 1
    prev_start, prev_end = ranges[0]

    while index < len(ranges):
        # print("idx: ", index)
        start, end = ranges[index]

        if prev_end >= start:
            # they are overlapping, we can merge them
            # print(f"{prev_end} is geq than the new start: {start}")
            prev_end = max(prev_end, end)

        else:
            counter += prev_end - prev_start + 1
            prev_start = start
            prev_end = end

        index += 1

    counter += prev_end - prev_start + 1
    return counter


def main():
    test_input = load_input(test=True)
    real_input = load_input()

    print("[test] part1:", part1(test_input))
    print("[real] part1:", part1(real_input))
    print("[test] part2:", part2(test_input))
    print("[real] part2:", part2(real_input))
    assert part2(real_input) == 338189277144473
    # 338189277144474 is too high
    # 338189277144473 is the answer


main()
