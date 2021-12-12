#!/usr/bin/python
#coding: utf8

def part1(filename: str) -> int:
    fuel_cost = []
    with open(filename) as f:
        positions = [int(pos) for pos in f.read().split(',')]
    for i in range(max(positions)+1):
        fuel = 0
        for pos in positions:
            if pos > i:
                fuel += pos - i
            else:
                fuel += i - pos
        fuel_cost.append(fuel)
    return min(fuel_cost)

if __name__ == '__main__':
    print("part1", part1("inputs/day7.txt"))