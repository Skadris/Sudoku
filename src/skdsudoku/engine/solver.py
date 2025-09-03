from typing import List, Optional, Tuple

from engine.board import Board
from validator import is_valid_move


def _find_empty_cell(board: Board) -> Optional[Tuple[int, int]]:
    """Find empty cell with fewest options remaining."""
    empties = board.empty_cells()
    if not empties:
        return None

    best_cell = None
    best_candidates = 10  # More than the maximum possible candidates (1-9)
    for r, c in empties:
        candidates = [v for v in range(1, 10) if is_valid_move(board, r, c, v)]
        if len(candidates) < best_candidates:
            best_candidates = len(candidates)
            best_cell = (r, c)
            if best_candidates == 1:
                break
    return best_cell


def solve_sudoku(board: Board) -> Optional[Board]:
    """Return a solved Sudoku board or None if unsolvable."""
    cell = _find_empty_cell(board)
    if cell is None:
        return board

    r, c = cell
    for v in range(1, 10):
        if is_valid_move(board, r, c, v):
            solved = solve_sudoku(board.set(r, c, v))
            if solved is not None:
                return solved
    return None


def has_unique_solution(board: Board) -> bool:
    """Check if the sudoku board has a unique solution."""
    solutions = 0

    def backtrack(b: Board) -> bool:
        nonlocal solutions
        cell = _find_empty_cell(b)
        if cell is None:
            solutions += 1
            return solutions > 1

        r, c = cell
        for v in range(1, 10):
            if is_valid_move(b, r, c, v):
                if backtrack(b.set(r, c, v)):
                    return True
        return False
    
    backtrack(board)
    return solutions == 1
