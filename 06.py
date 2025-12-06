Grid = list[list[str]]


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
        op = column[-1]
        # TODO: rewrite using import operator
        if op == "*":
            score = 1
            for n in column[:-1]:
                score *= int(n)
        else:
            score = 0
            for n in column[:-1]:
                score += int(n)

        # print(f"{i}th column score: {score}")
        result += score

    return result

def part2(grid: Grid) -> int:
    w = len(grid[0])
    result = 0
    for i in range(w):
        column = list(map(lambda row: row[i], grid))
        op = column[-1]
        # TODO: rewrite using import operator
        if op == "*":
            score = 1
            # TODO [part2]: now we need to go column by column
            for n in column[:-1]:
                score *= int(n)
        else:
            score = 0
            for n in column[:-1]:
                score += int(n)

        # print(f"{i}th column score: {score}")
        result += score

    return result



input = load_input()
print(part1(input))

input = load_input(test=False)
print(part1(input))
