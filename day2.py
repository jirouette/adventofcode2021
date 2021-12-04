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

def part2(filename: str) -> Tuple[int, int]:
    X = 0
    Y = 0
    aim = 0
    with open(filename) as f:
        for line in f:
            match line.split():
                case ["forward", x]:
                    X += int(x)
                    Y += aim*int(x)
                case ["down", y]:
                    aim += int(y)
                case ["up", y]:
                    aim -= int(y)
    return X, Y

if __name__ == '__main__':
    X, Y = part1("inputs/day2.txt")
    print("part1", X, "×", Y, "=", X*Y)
    X, Y = part2("inputs/day2.txt")
    print("part2", X, "×", Y, "=", X*Y)