from operator import mul
from math import sqrt, pow

from santa import reduce


Coords = tuple[int, int, int]


def load_input(test: bool = True) -> list[Coords]:
    with open(f"inputs/08{'-test' if test else ''}.txt") as file:
        return [
            tuple(map(int, line.strip().split(",")))
            for line
            in file.readlines()
        ]


def dist(c1: Coords, c2: Coords) -> float:
    d = 0
    for a1, a2 in zip(c1, c2):
        d += pow(a1 - a2, 2)

    return sqrt(d)



# TODO: this is a classic union-find problem, let's revisit that in a while


def part1(coords: list[Coords], limit: int = 10):
    # [(distance, c1, c2), ...]
    distances = {}
    for c1 in coords:
        for c2 in coords:
            if c1 == c2:  # do not compare with it own self
                continue

            dk = distances.keys()
            if (c1, c2) in dk or (c2, c1) in dk:
                continue

            # print(f"f: {c1}, s: {c2}")

            d = dist(c1, c2)
            distances[(c1, c2)] = d


    # take 10 shortest
    sorted_ = sorted(distances.items(), key=lambda p: p[1])
    # print(sorted_)
    to_match = sorted_[:limit]

    # print(to_match)

    groups = []

    # now create a groups out of 10 shortest paths
    for pair, _distance in to_match:
        c1, c2 = pair

        c1_group = None
        c2_group = None
        for g in groups:
            if c1 in g:
                c1_group = g

            if c2 in g:
                c2_group = g

        if c1_group is None and c2_group is None:
            # create new group
            groups.append((c1, c2))

        elif c1_group == c2_group:
            # nothing to do, they are existing already
            continue

        else:
            # merge group 1 with group 2
            if not c1_group:
                c1_group = (c1,)

            if c1_group in groups:
                groups.remove(c1_group)

            if not c2_group:
                c2_group = (c2,)

            if c2_group in groups:
                groups.remove(c2_group)


            new_group = tuple(set(c1_group + c2_group))
            groups.append(new_group)


    # # mul together top three groups
    top = sorted(groups, key=len, reverse=True)[:3]
    # print(top)
    return reduce(mul, list(map(len, top)))


def part2(coords: list[Coords]):
    # [(distance, c1, c2), ...]
    distances = {}
    for c1 in coords:
        for c2 in coords:
            if c1 == c2:  # do not compare with it own self
                continue

            dk = distances.keys()
            if (c1, c2) in dk or (c2, c1) in dk:
                continue

            # print(f"f: {c1}, s: {c2}")

            d = dist(c1, c2)
            distances[(c1, c2)] = d


    to_match = sorted(distances.items(), key=lambda p: p[1])
    groups = []

    result_xs = 0

    for pair, _distance in to_match:
        c1, c2 = pair

        c1_group = None
        c2_group = None
        for g in groups:
            if c1 in g:
                c1_group = g

            if c2 in g:
                c2_group = g

        if c1_group is None and c2_group is None:
            # create new group
            groups.append((c1, c2))

        elif c1_group == c2_group:
            # nothing to do, they are existing already
            continue

        else:
            # merge group 1 with group 2
            if not c1_group:
                c1_group = (c1,)

            if c1_group in groups:
                groups.remove(c1_group)

            if not c2_group:
                c2_group = (c2,)

            if c2_group in groups:
                groups.remove(c2_group)


            new_group = tuple(set(c1_group + c2_group))

            # TODO: I don't like it, it was slow a bit
            if len(new_group) == len(coords):  # if all of the coordinates has been assigned to any group
                result_xs = c1[0] * c2[0]
            groups.append(new_group)


    return result_xs


input = load_input()
print(part1(input))

input = load_input(test=False)
print(part1(input, limit=1000))

input = load_input()
print(part2(input))

input = load_input(test=False)
print(part2(input))
