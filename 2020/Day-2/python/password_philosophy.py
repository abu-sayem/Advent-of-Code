# SPDX-License-Identifier: MIT
# Copyright (c) 2020 abu-sayem
#
#https://adventofcode.com/2020/day/2


def readFile() -> list:
    input = []
    with open(f"input.txt", "r") as f:
        for line in f.readlines():
            str = line.split()
            max_min = str[0].split('-')
            input.append((int(max_min[0]), int(max_min[1]), str[1][:-1], str[2]))
        return input


# valid_password_count return total valid password number
def valid_password_count(vals: list) -> int:
    count = 0
    for val in vals:
        min, max, char, password = val
        if min <= password.count(char) <= max:
            count +=1
    return count
    

# valid_password_count return total valid password number validated by updated number
def valid_password_count_part_two(vals: list) -> int:
    count = 0
    for val in vals:
        min, max, char, password = val
        if (password[min-1]==char) ^ (password[max-1]==char):
            count +=1
    return count


if __name__ == "__main__":
    vals = readFile()
    print(len(vals))
    print(valid_password_count(vals))
    print(f"Part 1: {valid_password_count(vals)}")
    print(f"Part 2: {valid_password_count_part_two(vals)}")
