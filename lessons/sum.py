"""Practicing for loops and comparing them to other iterations."""

__author__ = "730710742"


def w_sum(vals: list[float]) -> float:
    """A function that uses a while loop to iternate through a list of floats and return their sumation."""
    index: int = 0
    sumation: float = 0
    while index < len(vals):
        sumation += vals[index]
        index += 1
    return sumation


def f_sum(vals: list[float]) -> float:
    """A function that uses a for loops to iterate through a list of floats to return the sumation of its values."""
    sumation: float = 0
    for number in vals:
        sumation += number
    return sumation


def f_range_sum(vals: list[float]) -> float:
    """A function that uses a for in range loop to iterate through a list of floats to return their sumation."""
    sumation: float = 0
    for index in range(0, len(vals)):
        sumation += vals[index]
    return sumation