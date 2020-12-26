# SPDX-License-Identifier: MIT
# Copyright (c) 2020 abu-sayem
#
#https://adventofcode.com/2020/day/2


def readFile() -> list:
    with open(f"input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]


def count_tree(vals: list, dx: int, dy:int) -> int:
    x, y, count, length, mod = 0, 0, 0, len(vals) - dy, len(vals[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if vals[y][x] == "#":
            count += 1
    return count



def part1(vals: list) -> int:
    return count_tree(vals, 3, 1)

def part2(vals: list, sol_part1:int):
    answer = sol_part1
    deltas = ((1,1), (5,1), (7,1), (1,2))
    for delta in deltas:
        answer *= count_tree(vals, delta[0], delta[1])
    return answer


if __name__ == "__main__":
    vals = readFile()
    sol_part1 = part1(vals)
    print(f"Part 1: {sol_part1}")
    print(f"Part 2: {part2(vals, sol_part1)}")
