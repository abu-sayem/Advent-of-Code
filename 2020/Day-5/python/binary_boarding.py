# SPDX-License-Identifier: MIT
# Copyright (c) 2020 abu-sayem
#
#https://adventofcode.com/2020/day/4



def readFile() -> list:
    vals = list()
    with open(f"{__file__.rstrip('binary_boarding.py')}input.txt", "r") as f:
        for data in f.read().split('\n'):
            vals.append(data)
    return vals


def find_id(code, lo, hi):
    for i in range(len(code)):
        mid = (lo + hi) // 2
        if code[i] == 'B' or code[i] == 'R':
            lo = mid + 1
        else:
            hi = mid 
    return (lo + hi) // 2
        
    

def part1(codes: list, seat_ids) -> int:
    for code in codes:
        row, column = find_id(code[:7], 0, 127), find_id(code[7:], 0, 7)
        seat_ids.append(row * 8 + column)
    return max(seat_ids)

def part2(seat_ids: list) -> int:
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids and (i + 1) in seat_ids and (i - 1) in seat_ids:
            return i



if __name__ == "__main__":
    inputs = readFile()
    seat_ids = list()
    ans = float('-inf')
    print(f"Part 1: {part1(inputs, seat_ids)}")
    print(f"Part 2: {part2(seat_ids)}")

