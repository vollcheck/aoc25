from functools import partial
from collections.abc import Iterable
from operator import add, mul


Grid = list[list[str]]

# NOTE: candidate for standard library
# TODO: -> int is not flexible enough
def reduce(f: callable, coll: Iterable) -> int:
    if not coll:
        return None

    # hack around mul
    acc = coll[0]
    for e in coll[1:]:
        acc = f(acc, e)

    return acc

def load_input(test: bool = True) -> Grid:
    result: list[list[int]] = []
    with open(f"inputs/06{'-test' if test else ''}.txt", "r") as file:
        for line in file.readlines():
            result.append(line.split())

    return result


def part1(grid: Grid) -> int:
    w = len(grid[0])
    result = 0
    for i in range(w):
        column = list(map(lambda row: row[i], grid))
        op = mul if column[-1] == "*" else add

        numbers = list(map(int, column[:-1]))
        result += reduce(op, numbers)
        # print(f"{i}th column score: {score}")

    return result


def align(to_len: int, number: str) -> str:
    cur_len = len(number)
    zeros = to_len - cur_len
    if zeros < 0:
        raise ValueError("cannot create negative chars")

    zeros_str = "0" * zeros
    return number + zeros_str


def ss_to_int(string_numbers: list[str]) -> int:
    return int("".join(n for n in string_numbers))


TEST_2 = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]

def part2(test: bool = True) -> int:
    # I have an issue with Emacs stripping lines automatically
    # if test:
    #     lines = TEST_2
    # else:
    #     with open("inputs/06-no-strip.txt", "r") as file:
    #         lines: list[str] = file.readlines()
    with open("inputs/06-no-strip.txt", "r") as file:
        lines: list[str] = file.readlines()

    result = 0
    w = len(lines[0])

    group: list[int] = []
    op = None

    for i in range(w):
        column = [row[i] for row in lines]

        breaking = all([x == " " for x in column])
        if breaking:
            print(f"found break, current group: {group} and op: {op}")
            result += reduce(op, group)  # TODO: fix this

            # reset
            group = []
            op = None

        else:
            next_op = column[-1]
            if not op and next_op != " ":
                op = mul if next_op == "*" else add

            g = "".join(c for c in column[:-1] if c != "\n")
            if g:
                group.append(int(g))

    result += reduce(op, group)  # TODO: fix this

    return result



# input = load_input()
# result = part1(input)
# print(result)
# assert result == 4277556

# input = load_input(test=False)
# result = part1(input)
# print(result)
# assert result == 6725216329103

input = load_input()
result = part2(input)
print(result)

input = load_input(test=False)
result = part2(input)
print(result)
