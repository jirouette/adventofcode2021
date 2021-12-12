#!/usr/bin/python
#coding: utf8

def part1(filename: str) -> int:
    nb_known_digits = 0
    with open(filename) as f:
        for line in f:
            digits = line.split(' | ')[1].split()
            for digit in digits:
                if len(digit) in [7, 4, 3, 2]:
                    nb_known_digits += 1
    return nb_known_digits

if __name__ == '__main__':
    print("part1", part1("inputs/day8.txt"))