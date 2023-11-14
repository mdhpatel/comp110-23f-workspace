"""Implementing algorithms to practice utility fucntions with lists."""

__author__ = "730710742"


def all(integer_list: list[int], search_integer: int) -> bool:
    """Returns true or false depending on whether or not all the integers in a list equal another given integr."""
    index: int = 0
    if len(integer_list) == 0:
        return False
    while index < len(integer_list):
        if (integer_list[index] != search_integer):
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer found in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_int: int = input[0]
    while index < len(input):
        if max_int < input[index]:
            max_int = input[index]
        index += 1
    return max_int


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Rteurns true or flase depesning on if the two given lists are equal to each other."""
    index: int = 0
    if len(list_one) != len(list_two):
        return False
    while index < len(list_one):
        if (list_one[index] != list_two[index]):
            return False
        index += 1
    return True
