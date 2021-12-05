#!/usr/bin/python
#coding: utf8

def compute_points(filename: str, part2: bool = False) -> int:
    diagram = dict()
    with open(filename) as f:
        for line in f:
            point1, point2 = line.split(' -> ')
            x1, y1 = [int(p) for p in point1.split(',')]
            x2, y2 = [int(p) for p in point2.split(',')]
            point = None
            if x1 == x2:
                if y1 > y2:
                    for i in range(y1 - y2 +1):
                        point = (x1, y2 + i,)
                        diagram[point] = diagram.get(point, 0) + 1
                else:
                    for i in range(y2 - y1 +1):
                        point = (x1, y1 + i,)
                        diagram[point] = diagram.get(point, 0) + 1
            elif y1 == y2:
                if x1 > x2:
                    for i in range(x1 - x2 +1):
                        point = (x2 + i, y1,)
                        diagram[point] = diagram.get(point, 0) + 1
                else:
                    for i in range(x2 - x1 +1):
                        point = (x1 + i, y1,)
                        diagram[point] = diagram.get(point, 0) + 1
            elif part2:
                if x1 > x2:
                    for i in range(x1 - x2 +1):
                        if y1 > y2:
                            point = (x2 + i, y2 + i,)
                        else:
                            point = (x2 + i, y2 - i,)
                        diagram[point] = diagram.get(point, 0) + 1
                else:
                    for i in range(x2 - x1 +1):
                        if y1 > y2:
                            point = (x1 + i, y1 - i,)
                        else:
                            point = (x1 + i, y1 + i,)
                        diagram[point] = diagram.get(point, 0) + 1
    points = 0
    for i in diagram.values():
        if i >= 2:
            points += 1
    return points

if __name__ == '__main__':
    print("part1", compute_points("inputs/day5.txt"))
    print("part2", compute_points("inputs/day5.txt", part2=True))
