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

PART2_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}
def part2(filename: str) -> int:
    scores = []
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
                    break
            else:
                line_score = 0
                for e in expecting[::-1]:
                    line_score *= 5
                    line_score += PART2_SCORE[e]
                scores.append(line_score)
    scores.sort()
    return scores[int(len(scores)/2)]

if __name__ == '__main__':
    print("part1", part1("inputs/day10.txt"))
    print("part2", part2("inputs/day10.txt"))
