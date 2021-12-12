#!/usr/bin/python
#coding: utf8

def part1(filename: str, nb_days: int) -> int:
    with open(filename) as f:
        state = [int(fish) for fish in f.read().split(',')]
    for day in range(nb_days):
        add = 0
        for key, _ in enumerate(state):
            state[key] -= 1
            if state[key] < 0:
                add += 1
                state[key] = 6
        for _ in range(add):
            state.append(8)
    return len(state)

if __name__ == '__main__':
    print("part1", part1("inputs/day6.txt", 80))