#!/usr/bin/python
#coding: utf8

MATCHING = {'(': ')', '{': '}', '<': '>', '[': ']'}
SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
def part1(filename: str) -> int:
    score = 0
    with open(filename) as f:
        for line in f:
            expecting = []
            for c in line[:-1]:
                if expecting and c == expecting[-1]:
                    expecting.pop()
                elif c in MATCHING.keys():
                    expecting.append(MATCHING[c])
                else:
                    print("Expecting", expecting[-1], "received", c)
                    score += SCORE.get(c, 0)
                    break
    return score

if __name__ == '__main__':
    print("part1", part1("inputs/day10.txt"))
