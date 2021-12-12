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

def part2(filename: str, nb_days: int) -> int:
    state = {i: 0 for i in range(9)}
    with open(filename) as f:
        for fish in f.read().split(','):
            state[int(fish)] += 1
    for day in range(nb_days):
        next = 0
        for key in list(range(9))[::-1]:
            next, state[key] = state[key], next
        state[8] += next
        state[6] += next
    return sum(state.values())


if __name__ == '__main__':
    print("part1", part1("inputs/day6.txt", 80))
    print("part2", part2("inputs/day6.txt", 256))