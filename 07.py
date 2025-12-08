from functools import cache


Grid = list[str]

def load_input(test: bool = True) -> Grid:
    with open(f"inputs/07{'-test' if test else ''}.txt") as file:
        lines = file.readlines()

    return lines


def part1(grid: Grid) -> int:
    # localize start - "S"
    # keep current beams - I guess we need only a width of them

    first_row = grid[0]
    w = len(first_row)

    starting_point = first_row.index("S")

    def split_beams(beams: set[int], splitters: list[int]) -> (set[int], int):
        # NOTE: this is not optimal
        times = 0
        result = set()
        for b in beams:
            if b in splitters:
                times += 1
                if b-1 >= 0:
                    result.add(b-1)
                if b+1 < w:
                    result.add(b+1)
            else:
                result.add(b)

        return result, times


    # list of current beams width really
    beams: set[int] = {starting_point}
    times = 0

    for row in grid[1:]:
        splitters = [i for i, c in enumerate(row) if c == "^"]
        beams, another_times = split_beams(beams, splitters)
        times += another_times

    return times


def part2_recursive(grid: Grid) -> int:
    first_row = grid[0]
    w = len(first_row)
    h = len(grid)
    starting_point = first_row.index("S")

    @cache
    def aux(x: int, y: int) -> int:
        if y >= h:
            return 1

        candidates = []
        if grid[y][x] == "^":
            if x-1 >= 0:
                candidates.append((x-1, y+1))  # has left
            if x+1 < w:
                candidates.append((x+1, y+1))  # has right

        else:
            candidates.append((x, y+1))  # simply go down

        return sum(aux(nx, ny) for nx, ny in candidates)

    return aux(starting_point, 1)


input = load_input()
print(part1(input))

input = load_input(test=False)
print(part1(input))

input = load_input()
print(part2_recursive(input))

input = load_input(test=False)
print(part2_recursive(input))

# 21
# 1656
# 40
# 76624086587804
