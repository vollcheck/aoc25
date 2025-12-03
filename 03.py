def parse_input(test: bool = True) -> list[list[int]]:
    lines = []
    with open(f"inputs/03{'-test' if test else ''}.txt") as f:
        for line in f.readlines():
            lines.append(list(map(int, line.strip())))  # list needed?

    return lines


# NOTE: candidate for aoc standard library
def concatenate_int(array: list[int]) -> int:
    # NOTE: I wonder if dealing with pow of 10 and reducing (summing)
    # would be more efficient
    return int("".join([i for i in array]))

def max_number(line: list[int]) -> int:
    m1 = 0
    m2 = 0
    for i, n in enumerate(line):
        # if new max and space for another candidate
        if n > m1 and i < len(line) - 1:
            m1 = n
            m2 = line[i+1]
        elif n > m2:
            m2 = n

    return int(f"{m1}{m2}")
    # return concatenate_int([m1, m2])


# TODO: that could be applied to the first part as well, just with a 2 instead of 12 elements
def max_number12(line: list[int]) -> int:
    # let's say we want to accomodate N elements
    # for this particular exercise N=12
    # so my plan is following:
    # look for the biggest int in the line,
    # but only line[:len(line)-N]  # or maybe N-1
    # so -N because we need to have space for N
    # elements through the end of the line.
    # then, in next loop, we subtract 1 from N
    # (for our example it makes it N=11 effectively)
    # repeating the logic:
    # - find the biggest int, but leaving N-1 elements from end
    #   leaving a reservoir for other elements
    # - proceed with N-1-1 loop run

    N = 12  # TODO: provide it later as an argument

    agg: list[int] = []
    size = len(line)  # NOTE: that could've been hardcoded, it differs only for test/real input, otherwise all lines are the same length

    prev_index = None
    for i in range(N):
        index = prev_index or 0
        # print(f"starting fresh with index {index}")
        m = (0, index)  # max value, index)
        line_end = size - (N - i) + 1
        # print(f"line end for {i}th element is {line_end}")
        while index < line_end:
            line_element = line[index]
            if line_element > m[0]:
                # print(f"found next big number: current {m[0]} vs {line_element}")
                m = (line_element, index)

            # print(f"currently at {index} with {line_element} value")
            index += 1

        # print(f"ended loop with: {m}")
        # TODO: WE MUST KEEP AN INDEX OF previously find MAX VALUE and start from there
        prev_index = m[1] + 1
        agg.append(m[0])

    return int("".join([str(d) for d in agg]))


def solve(f: callable, data: list[list[int]]) -> int:
    return sum([f(line) for line in data])

def main():
    test_input = parse_input(test=True)
    real_input = parse_input(test=False)
    print(f"[test] Part 1: {solve(max_number, test_input)}")
    print(f"[real] Part 1: {solve(max_number, real_input)}")
    print(f"[test] Part 2: {solve(max_number12, test_input)}")
    print(f"[real] Part 2: {solve(max_number12, real_input)}")
    assert solve(max_number, test_input) == 357
    assert solve(max_number, real_input) == 17405
    assert part2(test_input) == 3121910778619
    assert part2(real_input) == 171990312704598


if __name__ == "__main__":
    main()

main()
# 17372 is too low
