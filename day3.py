#!/usr/bin/python
#coding: utf8

from typing import Tuple

def find_most(l: list, el) -> True:
    return l.count(el) >= len(l)/2

def find_least(l: list, el) -> True:
    return l.count(el) <= len(l)/2

def part1(filename: str) -> Tuple[int, int]:
    columns = []
    with open(filename) as f:
        for line in f:
            for i in range(len(line)-1):
                if len(columns) <= i:
                    columns.append(list())
                columns[i].append(line[i])
    gamma = ""
    epsilon = ""
    for column in columns:
        gamma += "1" if find_most(column, "1") else "0"
        epsilon += "0" if gamma[-1] == "1" else "1"
    return int(gamma, 2), int(epsilon, 2)

def part2(filename: str) -> Tuple[int, int]:
    columns = []
    nb_bits = 0
    with open(filename) as f:
        for line in f:
            nb_bits = len(line)-1
            break
        f.seek(0)
        kept_oxygen_numbers = [list(line[:-1]) for line in f]
        f.seek(0)
        kept_CO2_numbers = [list(line[:-1]) for line in f]
        for i in range(nb_bits):
            most_common = "1" if find_most([line[i] for line in kept_oxygen_numbers], "1") else "0"
            least_common = "0" if find_least([line[i] for line in kept_CO2_numbers], "0") else "1"
            if len(kept_oxygen_numbers) > 1:
                kept_oxygen_numbers = [line for line in kept_oxygen_numbers if line[i] == most_common]
            if len(kept_CO2_numbers) > 1:
                kept_CO2_numbers = [line for line in kept_CO2_numbers if line[i] == least_common]
        return int("".join(kept_oxygen_numbers[0]), 2), int("".join(kept_CO2_numbers[0]), 2)



if __name__ == '__main__':
    g, e = part1("inputs/day3.txt")
    print("part1", g, "×", e, "=", g*e)
    o, c = part2("inputs/day3.txt")
    print("part2", o, "×", c, "=", o*c)
