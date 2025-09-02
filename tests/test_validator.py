from skdsudoku.engine.board import Board
from skdsudoku.engine.validator import is_complete, is_valid_board, is_valid_move

solved_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]

def test_is_valid_move():
    b = Board()
    assert is_valid_move(b, 0, 0, 5) is True  

def test_is_valid_move_box_conflict():
    b = Board()
    b = b.set(0, 0, 5)
    assert is_valid_move(b, 1, 1, 5) is False

def test_is_not_valid_move():
    b = Board()
    assert is_valid_move(b, 0, 0, 10) is False
    b = b.set(0, 0, 5)
    assert is_valid_move(b, 0, 0, 5) is False

def test_is_valid_board():  
    b = Board()
    assert is_valid_board(b) is True
    b = b.set(0, 0, 5).set(0, 1, 5)
    assert is_valid_board(b) is False

def test_is_valid_board_box_duplicate():
    b = Board()
    b = b.set(0, 0, 5).set(1, 1, 5)
    assert is_valid_board(b) is False

def test_is_valid_board_column_duplicate():
    b = Board()
    b = b.set(0, 0, 5).set(1, 0, 5)
    assert is_valid_board(b) is False

def test_is_valid_board_bad():
    b = Board.from_rows(solved_board)
    b = b.set(0, 0, 9)
    assert is_valid_board(b) is False

def test_is_complete():    
    b = Board.from_rows(solved_board)
    assert is_complete(b) is True

def test_is_complete_incomplete_board():
    b = Board()
    assert is_complete(b) is False
    b = b.set(0, 0, 5)
    assert is_complete(b) is False
    