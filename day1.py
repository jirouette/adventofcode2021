#!/usr/bin/python
#coding: utf8

def part1(filename: str) -> int:
    nb_of_increases = 0
    last_measurement = 999999 # max
    with open(filename) as f:
        for line in f:
            measurement = int(line)
            if measurement > last_measurement:
                nb_of_increases += 1
            last_measurement = measurement
    return nb_of_increases

def part2(filename: str) -> int:
    nb_of_increases = 0
    last_measurement = 999999 # max
    with open(filename) as f:
        lines = [int(line) for line in f]
    for i in range(len(lines)-2):
        measurement = sum(lines[i:i+3])
        if measurement > last_measurement:
            nb_of_increases += 1
        last_measurement = measurement
    return nb_of_increases


if __name__ == '__main__':
    print("part1", part1("inputs/day1.txt"))
    print("part2", part2("inputs/day1.txt"))
