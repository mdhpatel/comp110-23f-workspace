"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Implementation of and creation of methods for the Simpy program."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, vals: list[float]):
        """The constructor for creating aa simpy object."""
        self.values = vals

    def __str__(self) -> str:
        """Creates a string representing simpy and its values within its list."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, values_filled: int) -> None:
        """Fills a specified number of indeces in simpy with a certain value."""
        index: int = 0
        new_list: list[float] = []
        while index < values_filled:
            new_list.append(fill_value)
            index += 1
        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Adds a range of values to a list of values and returns it."""
        assert step != 0.0
        new_list: list[float] = []
        if step > 0:
            while start < stop:
                new_list.append(start)
                start += step
        else:
            while start > stop:
                new_list.append(start)
                start += step
        self.values = new_list

    def sum(self) -> float:
        """Adsds up all the values in the values list and then returns that decimal."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition overrifde operator that adds a float or a Simpy to another Simpy."""
        new_object: Simpy = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                elem += rhs
                new_object.values.append(elem)
        else: 
            assert len(self.values) == len(rhs.values)
            for val in range(0, len(self.values)):
                self.values[val] += rhs.values[val]
                new_object.values.append(self.values[val])
        return new_object
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Makes a float or Simpy to the power of a simpy."""
        new_object: Simpy = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                elem **= rhs
                new_object.values.append(elem)
        else: 
            assert len(self.values) == len(rhs.values)
            for val in range(0, len(self.values)):
                self.values[val] **= rhs.values[val]
                new_object.values.append(self.values[val])
        return new_object
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two Simpy objects and makes a new list of booleans depending on if the values of both lists are equal."""
        equality_list: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                if val == rhs:
                    equality_list.append(True)
                else:
                    equality_list.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for elem in range(len(self.values)):
                if self.values[elem] == rhs.values[elem]:
                    equality_list.append(True)
                else:
                    equality_list.append(False)
        return equality_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares a Simpy object to another Simpy or a float to create a list of booleans showing what values are greater than others."""
        equality_list: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                if val > rhs:
                    equality_list.append(True)
                else:
                    equality_list.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for val in range(len(self.values)):
                if self.values[val] > rhs.values[val]:
                    equality_list.append(True)
                else:
                    equality_list.append(False)
        return equality_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This code returns the value of Simpy at a certain given index."""
        new_obj: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            index: int = 0
            while index < len(self.values):
                if rhs[index] is True:
                    new_obj.values.append(self.values[index])
                index += 1
            return new_obj