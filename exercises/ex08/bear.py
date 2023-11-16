"""File to define Bear class."""


class Bear:
    """This class creates the object and methods used by bear."""

    age: int
    hunger_score: int
    
    def __init__(self, age_init: int = 0, hunger_score_init: int = 0):
        """The constructor for the bear object."""
        self.age = age_init
        self.hunger_score = hunger_score_init
        return None
    
    def one_day(self):
        """This increases the age of a bear by one year and decreases a bear's hunger by 1 as well."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """This increases a bear's hunger score by the amount of fish that the bear consumed."""
        self.hunger_score += num_fish