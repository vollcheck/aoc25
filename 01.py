test_input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

with open("inputs/01.txt", "r") as file:
    real_input = file.readlines()


def part1(steps: list[int]) -> int:
    rotations = 0
    state = 50
    for step in steps:
        dir = step[0]
        amount = int(step[1:])
        # print(dir, amount)
        if dir == "R":
            state = (state + amount) % 100
        else:
            state = (state - amount) % 100

        if state == 0:
            rotations += 1

    return rotations

def part2(steps: list[int]) -> int:
    rotations = 0
    state = 50
    for step in steps:
        dir = step[0]
        amount = int(step[1:])
        # print(dir, amount)

        # NOTE: it is a bruteforce solution, I'm not happy with it but it is what it is
        for _ in range(amount):
            if dir == "R":
                state += 1
            else:
                state -= 1
            state %= 100

            if state == 0:
                rotations += 1

    return rotations

def part2_arithmetic(steps: list[int]) -> int:
    from operator import add, sub

    rotations = 0
    state = 50
    for step in steps:
        dir = step[0]
        amount = int(step[1:])
        # print(dir, amount)
        op = add if dir == "R" else sub

        quot, rem = divmod(op(state, amount), 100)


        # so the problem with an arithmetic solution is that there might be a various
        # edge cases that are hard to cover:
        # 1. you stepped on 0 from one side, increase rotation count and stop, but in next step you move out from 0
        #    to the same direction as previously, so again, for one crossing, you get two rotations
        # 2. you stepped on 0 from one side, increase rotation count and stop, but in next step you move out from 0
        #    to opposite direction than previously, so for one crossing you get two rotations
        rotations += abs(quot)
        if rem == 0 and abs(quot) > 0:
            rotations -= 1
        state = rem

    return rotations



# 6236 too small
# 6272 too much
# 6254 is an exact answer

def main():
    # print(f"[test] Part 1: {part1(test_input)}")
    # print(f"[real] Part 1: {part1(real_input)}")
    print(f"[test] Part 2: {part2(test_input)}")
    print(f"[real] Part 2: {part2(real_input)}")
    print(f"[test] experimental: {part2_arithmetic(test_input)}")
    print(f"[real] experimental: {part2_arithmetic(real_input)}")

if __name__ == "__main__":
    main()

main()
