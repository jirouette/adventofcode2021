#!/usr/bin/python
#coding: utf8

from dataclasses import dataclass

@dataclass
class NumberCase:
    nb: int
    is_marked: bool = False

    def __repr__(self):
        return str(self.nb)

def build_board(payload: str) -> dict:
    payload = payload.replace("  ", " ").split("\n")
    board = dict()
    y = 0
    for line in payload:
        x = 0
        for nb in line.split():
            board[x, y] = NumberCase(int(nb))
            x += 1
        y += 1
    return board

def get_boards(payload: str) -> list[dict]:
    boards = "\n".join(payload.split("\n")[2:]).split("\n\n")
    return [build_board(board) for board in boards]

def get_rolling_numbers(payload: str) -> list[int]:
    return [int(nb) for nb in payload.split("\n")[0].split(",")]

def is_winning_board(board: dict) -> bool:
    for i in range(5):
        winning = True
        for j in range(5):
            if not board.get((i, j,)).is_marked:
                winning = False
                break
        if winning:
            return True
    for i in range(5):
        winning = True
        for j in range(5):
            if not board.get((j, i,)).is_marked:
                winning = False
                break
        if winning:
            return True
    return False

def sum_unmarked(board: dict) -> bool:
    return sum([nb_case.nb for nb_case in board.values() if not nb_case.is_marked])

def part1(filename: str) -> int:
    with open(filename) as f:
        payload = f.read()
    boards = get_boards(payload)
    numbers = get_rolling_numbers(payload)
    for number in numbers:
        for board in boards:
            for nb_case in board.values():
                if nb_case.nb == number:
                    nb_case.is_marked = True
            if is_winning_board(board):
                return number * sum_unmarked(board)
    return 0

def part2(filename: str) -> int:
    with open(filename) as f:
        payload = f.read()
    boards = get_boards(payload)
    numbers = get_rolling_numbers(payload)
    winning_boards = []
    winning_numbers = []
    for number in numbers:
        for board in boards:
            if board in winning_boards:
                continue
            for nb_case in board.values():
                if nb_case.nb == number:
                    nb_case.is_marked = True
            if is_winning_board(board):
                winning_boards.append(board)
                winning_numbers.append(number)
    return winning_numbers[-1] * sum_unmarked(winning_boards[-1])


if __name__ == '__main__':
    print("part1", part1("inputs/day4.txt"))
    print("part2", part2("inputs/day4.txt"))
