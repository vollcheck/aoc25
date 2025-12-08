from collections.abc import Iterable


def reduce(f: callable, coll: Iterable) -> int:
    if not coll:
        return None

    # hack around mul
    acc = coll[0]
    for e in coll[1:]:
        acc = f(acc, e)

    return acc
