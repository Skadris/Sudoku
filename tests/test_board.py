import pytest

from skdsudoku.engine.board import Board


def test_board_init_and_get_set():
    """
    Scenario to test initializing board and getting/setting
    """
    b = Board()
    assert b.get(0, 0) == 0

    b2 = b.set(0, 0, 5)
    assert b.get(0, 0) == 0
    assert b2.get(0, 0) == 5


def test_board_shape_height():
    with pytest.raises(ValueError):
        Board([[0] * 9 for _ in range(8)])  # Board height - rows


def test_board_shape_width():
    with pytest.raises(ValueError):
        Board([[0] * 8 for _ in range(9)])  # Board width - cols


def test_board_value_range():
    with pytest.raises(ValueError):
        Board([[10] * 9 for _ in range(9)])


def test_box_values_and_empty_cells():
    """
    Scenario to test box values and empty cells
    """
    b = Board()
    b = b.set(1, 1, 4)
    assert 4 in b.box_values(2, 2)

    em = b.empty_cells()
    assert (1, 1) not in em
    assert len(em) == 80


def test_clear_cell():
    b = Board()
    b = b.set(2, 3, 5)
    assert 5 in b.box_values(2, 3)

    b = b.clear(2, 3)
    assert 5 not in b.box_values(2, 3)

