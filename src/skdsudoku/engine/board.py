from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

Grid = List[List[int]]

def _blank_grid() -> Grid:
    return [[0 for _ in range(9)] for _ in range(9)]

@dataclass
class Board:
    """
    Board model, provides methods for row/col/box access and updates.
    """

    grid: Grid = field(default_factory=_blank_grid)


    def __post_init__(self) -> None:
        """
        Checks if the Board object is valid.
        Checks if there are 9 rows and columns
        Checks if the values are between 0 and 9
        """
        if len(self.grid) != 9 or any(len(row) != 9 for row in self.grid):
            raise ValueError("Board must have 9 rows and 9 columns")
        for r in range(9):
            for c in range(9):
                v = self.grid[r][c]
                if not (0 <= v <= 9):
                    raise ValueError("Board cell value must be between 0 and 9")


    @staticmethod
    def from_rows(rows: Grid) -> "Board":
        """
        Ensure a deep copy of each row so Board owns its own grid safely
        """
        return Board([row[:] for row in rows])

    def copy(self) -> "Board":
        """
        Creates a new Board object with the same grid values as the current one
        """
        return Board.from_rows(self.grid)

    def get(self, r: int, c: int) -> int:
        """
        :return value at [row][col]
        """
        self._assert_rc(r, c)
        return self.grid[r][c]

    def set(self, r: int, c: int, value: int) -> "Board":
        """
        Creates a fresh copy of the current board and updates the cell in the copied board
        :return the modified board
        """
        self._assert_rc(r, c)
        if not (0 <= value <= 9):
            raise ValueError("value must be between 0 and 9")
        new = self.copy()
        new.grid[r][c] = value
        return new

    def clear(self, r: int, c: int) -> "Board":
        """
        Removes value at [row][col]
        """
        return self.set(r, c, 0)

    def row_values(self, r: int) -> List[int]:
        """
        :return: a list of 9 integers representing that row.
        """
        self._assert_r(r)
        return self.grid[r][:]

    def col_values(self, c: int) -> List[int]:
        """
        :return: a list of 9 integers representing that column.
        """
        self._assert_c(c)
        return [self.grid[r][c] for r in range(9)]

    def box_values(self, r: int, c: int) -> List[int]:
        """
        Get all values from the 3×3 box containing cell (r, c).
        """
        self._assert_rc(r, c)
        br = (r // 3) * 3
        bc = (c // 3) * 3
        return [self.grid[br+dr][bc+dc] for dr in range(3) for dc in range(3)]

    def empty_cells(self) -> List[Tuple[int, int]]:
        """
        Return a list of coordinates (r, c) where the board is empty (value == 0).
        """
        return [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0]

    def is_filled(self) -> bool:
        """
        :return: True if the entire Sudoku board has no empty cells.
        """
        return all(self.grid[r][c] != 0 for r in range(9) for c in range(9))

    def _assert_r(self, r: int) -> None:
        """
        Checks if the row object is valid.
        """
        if not (0 <= r <= 9):
            raise IndexError("row must be between 0 and 9")

    def _assert_c(self, c: int) -> None:
        """
        Checks if the column object is valid.
        """
        if not (0 <= c <= 9):
            raise IndexError("column must be between 0 and 9")

    def _assert_rc(self, r: int, c: int) -> None:
        """
        Checks if the Board cell is valid.
        """
        self._assert_r(r)
        self._assert_c(c)

    def __str__(self) -> str:
        lines = []
        for r in range(9):
            row = []
            for c in range(9):
                v = self.grid[r][c]
                row.append(str(v) if v != 0 else '.')
                if c % 3 == 2 and c != 8:
                    row.append('|')
            lines.append(''.join(row))
            if r % 3 == 2 and r != 8:
                lines.append('------+-------+------')
        return '\n'.join(lines)


