#!/usr/bin/python
#coding: utf8

from typing import Tuple

def find_most(l: list, el) -> True:
    return l.count(el) > len(l)/2

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

if __name__ == '__main__':
    g, e = part1("inputs/day3.txt")
    print("part1", g, "×", e, "=", g*e)
