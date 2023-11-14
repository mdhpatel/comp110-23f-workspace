"""Test my zip function."""

__author__ = "730710742"

from lessons.zip import zip


def test_empty_lists() -> None:
    """Zip of an empty lists shoudl return an empty dictionary."""
    assert zip([], [1, 2]) == {}


def test_list_of_three_elemnts() -> None:
    """Zip of equal length lists should return a dictionary."""
    assert zip(["Maanav", "Patel"], [0, 1]) == {"Maanav": 1, "Patel": 2}


def test_lonnger_lists() -> None:
    """Zip shoudl still return a dictionary regardless of the length of the lists."""
    assert zip(["Monday", "Tuesday", "Wednesday", "Thursday"], [0, 1, 2, 3]) == {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3}
