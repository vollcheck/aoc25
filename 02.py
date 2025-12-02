import re

Range = tuple[int, int]

def parse_input(test: bool = True) -> list[Range]:
    ranges: list[Range] = []
    with open(f"inputs/02{'-test' if test else ''}.txt") as f:
        for line in f.readlines():
            parts = line.strip().split(",")
            for part in parts:
                if part:
                    rng = tuple(map(int, part.split("-")))
                    ranges.append(rng)

    return ranges


def is_not_valid(value: int) -> bool:
    # a backreference pattern:
    # (.+) captures any sequence of characters
    # \1+ matches one or more repetitions of captured group
    return re.fullmatch(r"(.+)\1", str(value))

def is_not_valid_more(value: int) -> bool:
    # a backreference pattern again:
    # this time I added `{1,}` so it is required at least twice but can more
    return re.fullmatch(r"(.+)\1{1,}", str(value))

def process_ranges(f: callable, ranges: list[Range]) -> int:
    result = 0
    for start, end in ranges:
        # these ranges are inclusive of both ends!
        for number in range(start, end + 1):
            if f(number):
                result += number

    return result

def part1(ranges: list[Range]) -> int:
    return process_ranges(is_not_valid, ranges)

def part2(ranges: list[Range]) -> int:
    return process_ranges(is_not_valid_more, ranges)


def main():
    test_input = parse_input(test=True)
    real_input = parse_input(test=False)
    # print(f"[test] Part 1: {part1(test_input)}")
    # print(f"[real] Part 1: {part1(real_input)}")
    # print(f"[test] Part 2: {part2(test_input)}")
    # print(f"[real] Part 2: {part2(real_input)}")
    assert part1(test_input) == 4174379265
    assert part1(real_input) == 73694270688
    assert part2(test_input) == 4174379265
    assert part2(real_input) == 73694270688


if __name__ == "__main__":
    main()

main()
