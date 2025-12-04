Grid = list[list[str]]
Positions = list[tuple[int, int]]  # or char,char?

ROLL = "@"
RNG = [-1, 0, 1]

def load_input(test: bool = False) -> Grid:
    with open(f"inputs/04{'-test' if test else ''}.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def count_adjacents(grid: Grid, x, y) -> bool:
    h = len(grid)
    w = len(grid[0])

    counter = 0

    for ry in RNG:
        for rx in RNG:
            if ry == 0 and rx == 0:
                # we are interested in adjacents only
                continue

            nx = rx + x
            ny = ry + y

            if (0 <= nx < w) and (0 <= ny < h) and grid[ny][nx] == ROLL:
                    counter += 1

    # return 1 if counter < 4 else 0
    return counter < 4


def viz(grid: Grid, positions: Positions):
    for x, y in positions:
        row = list(grid[y])
        row[x] = "x"
        grid[y] = "".join([x for x in row])

    for row in grid:
        print(row)


def part1(grid: Grid) -> int:
    # TODO: we are getting it twice, smol' refactor maybe?
    h = len(grid)
    w = len(grid[0])

    pos = []
    counters = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == ROLL and count_adjacents(grid, x, y):
                counters += 1
                pos.append((x, y))


    # viz(grid, pos)
    # print(pos)

    return counters


def remove_rolls(grid: Grid, positions: Positions) -> Grid:
    for x, y in positions:
        row = list(grid[y])
        row[x] = "."
        grid[y] = "".join([x for x in row])

    return grid


def part2(grid: Grid) -> int:
    # TODO: we are getting it twice, smol' refactor maybe?
    h = len(grid)
    w = len(grid[0])

    removed_counter = 0

    while True:
        pos = []
        counters = 0

        for y in range(h):
            for x in range(w):
                if grid[y][x] == ROLL and count_adjacents(grid, x, y):
                    counters += 1
                    pos.append((x, y))

        if not pos:
            break

        removed_counter += len(pos)
        grid = remove_rolls(grid, pos)

    # viz(grid, pos)
    # print(pos)

    return removed_counter



def main():
    test_input = load_input(test=True)
    real_input = load_input()

    print("[test] part1:", part1(test_input))
    print("[real] part1:", part1(real_input))
    print("[test] part2:", part2(test_input))
    print("[real] part2:", part2(real_input))


main()
