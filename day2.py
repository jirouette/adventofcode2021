#!/usr/bin/python
#coding: utf8

from typing import Tuple


def part1(filename: str) -> Tuple[int, int]:
    X = 0
    Y = 0
    with open(filename) as f:
        for line in f:
            match line.split():
                case ["forward", x]:
                    X += int(x)
                case ["down", y]:
                    Y += int(y)
                case ["up", y]:
                    Y -= int(y)
    return X, Y

if __name__ == '__main__':
    X, Y = part1("inputs/day2.txt")
    print("part1", X, "×", Y, "=", X*Y)