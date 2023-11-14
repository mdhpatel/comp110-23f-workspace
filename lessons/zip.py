"""Combining two lists into a dictionary."""

__author__ = "730710742"


def zip(strings: list[str], integers: list[int]) -> dict[str, int]:
    """Creating a new ductionary with elemnts from two lists of strings and integers."""
    new_dict: dict[str, int] = dict()
    if (len(strings) != len(integers)) or (len(strings) == 0) or (len(integers) == 0):
        return new_dict
    for elem in range(0, len(strings)):
        new_dict[strings[elem]] = integers[elem]
    return new_dict