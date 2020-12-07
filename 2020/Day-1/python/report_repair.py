
# SPDX-License-Identifier: MIT
# Copyright (c) 2020 abu-sayem
#
#https://adventofcode.com/2020/day/1

def readFile() -> list:
    with open(f"input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

# Two sum: Find the two entries that sum to 2020 and multiply them by eachother
def two_sum(years: list) -> int:
    store = set()
    for year in years:
        if 2020 - year in store:
            return year * (2020 - year)
        else:
            store.add(year)


# Three sum: Find the two entries that sum to 2020 and multiply them by eachother
def three_sum(years: list) -> int:
    len_years = len( years )
    if len_years < 3:
        return None
    years.sort()
    for year1 in range(len_years - 2):
        year2 = year1 + 1
        year3 = len_years - 1
        while year2 < year3:
            sum3 = years[year1] + years[year2] + years[year3]
            if sum3 < 2020:
                year2 +=1
            elif sum3 > 2020:
                year3 -= 1
            else:
                return years[year1]  * years[year2] * years[year3]

if __name__ == "__main__":
    years = readFile()
    print(f"Part 1: {two_sum(years)}")
    print(f"Part 2: {three_sum(years)}")
