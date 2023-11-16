"""File to define Fish class."""


class Fish:
    """This creates the fish object."""
    
    age: int
    
    def __init__(self, age_init: int = 0):
        """The constructor for fish objects."""
        self.age = age_init
        return None
    
    def one_day(self):
        """This increases the age of a fish by one for ervery day that passes in the simulation."""
        self.age += 1
        return None