from __future__ import annotations

from typing import Iterable

from .board import Board


def no_duplicates(nums: Iterable[int]) -> bool:
    """
    :param nums: sequence of numbers (row, column, or box).
    :return: True if there are no duplicate non-zero values.
    """
    seen = set()
    for n in nums:
        if n == 0:
            continue
        if n in seen:
            return False
        seen.add(n)
    return True


def is_valid_move(board: Board, r: int, c: int, value: int) -> bool:
    """
    :param board: board object.
    :param r: row number.
    :param c: cell number.
    :param value: value to place (1...9)
    :return: True if the move is allowed under Sudoku rules.
    """
    if not (1 <= value <= 9):
        return False
    if board.get(r, c) not in (0,):
        return False
    row_ok = value not in board.row_values(r)
    col_ok = value not in board.col_values(c)
    box_ok = value not in board.box_values(r, c)
    return row_ok and col_ok and box_ok


def is_valid_board(board: Board) -> bool:
    """
    :param board: take a board object.
    :return: True if the board obey Sudoku rules.
    """
    for r in range(9):
        if not no_duplicates(board.get(r)):
            return False

    for c in range(9):
        if not no_duplicates(board.get(c)):
            return False

    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            if not no_duplicates(
                [board.grid[br + dr][bc + dc] for dr in range(3) for dc in range(3)]
            ):
                return False

    return True


def is_complete(board: Board) -> bool:
    """
    Checks if the board is complete.
    """
    return board.is_filled() and is_valid_board(board)
