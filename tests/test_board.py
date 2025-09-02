import pytest

from skdsudoku.engine.board import Board


def test_board_init_and_get_set():   
    b = Board()
    assert b.get(0, 0) == 0

    b2 = b.set(0, 0, 5)
    assert b.get(0, 0) == 0
    assert b2.get(0, 0) == 5

def test_set_and_clear_multiple_cells():
    b = Board() 
    b2 = b.set(0, 0 , 1).set(1, 1, 2).set(2, 2, 3)
    assert b2.get(0, 0) == 1
    assert b2.get(1, 1) == 2
    assert b2.get(2, 2) == 3
    b3 = b2.clear(1, 1).clear(2, 2)
    assert b3.get(0, 0) == 1
    assert b3.get(1, 1) == 0
    assert b3.get(2, 2) == 0

def test_board_shape_height():
    with pytest.raises(ValueError):
        Board([[0] * 9 for _ in range(8)])  # Board height - rows


def test_board_shape_width():
    with pytest.raises(ValueError):
        Board([[0] * 8 for _ in range(9)])  # Board width - cols


def test_board_value_range():
    with pytest.raises(ValueError):
        Board([[10] * 9 for _ in range(9)])

def test_invalid_indices():
    b = Board()
    with pytest.raises(IndexError):
        b.get(-1, 0)
    with pytest.raises(IndexError):
        b.get(0, 10)
    with pytest.raises(IndexError):
        b.set(9, 0, 5)
    with pytest.raises(IndexError):
        b.clear(0, -1)

def test_box_values_and_empty_cells():   
    b = Board()
    b = b.set(1, 1, 4)
    assert 4 in b.box_values(2, 2)

    em = b.empty_cells()
    assert (1, 1) not in em
    assert len(em) == 80

def test_rown_col_box_access():
    b = Board()
    b = b.set(0, 0, 5).set(0, 1, 3).set(1, 0, 6)
    assert b.row_values(0) == [5, 3] + [0]*7
    assert b.col_values(0) == [5, 6] + [0]*7
    assert set(b.box_values(0, 0)) == {5,3,6,0}

def test_clear_cell():
    b = Board()
    b = b.set(2, 3, 5)
    assert 5 in b.box_values(2, 3)

    b = b.clear(2, 3)
    assert 5 not in b.box_values(2, 3)

def test_empty_cells_partial():
    b = Board()
    b = b.set(0, 0, 5).set(1, 1, 3)
    em = b.empty_cells()
    assert len(em) == 79
    assert (0, 0) not in em
    assert (1, 1) not in em
    assert (0, 1) in em
    assert (8, 8) in em

def test_immutability():
    b = Board()
    b2 = b.set(0, 0, 7)
    assert b.get(0, 0) == 0
    assert b2.get(0, 0) == 7
    b3 = b2.clear(0, 0)
    assert b2.get(0, 0) == 7
    assert b3.get(0, 0) == 0
