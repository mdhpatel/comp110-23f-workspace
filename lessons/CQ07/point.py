"""Practicing Classes and their creation and applications."""

from __future__ import annotations

__author__ = "730710742"


class Point:
    """This class creates the attributes and methods to go along with Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """The code for creating my constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Multiplies x and y by a certain factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Makes a new point with existing Point's factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Magic ethod to make the points print in a readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method to make the multilpication sign be used to multiply and craete a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Magic method that creates a new point and adds a certain given factor to those points."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point