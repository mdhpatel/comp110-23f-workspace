"""Defining A Class!"""

from __future__ import annotations

class Pizza:

    #attributes
    #Think of these as the variables each instance of my class will have
    #<name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, input_size: str, input_toppings: int, inp_gf: bool):
        """My constructor."""
        self.size = input_size
        self.toppings = input_toppings
        self.gluten_free = inp_gf
        # returns a Pizza object by nature of this method

    def price(self) -> float:
        """Caulate The Price of A Pizza."""
        if self.size == "large":
            price: float = 6.25
        else: 
            price: float = 5.00
        price += 0.75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, number_toppings: int):
        """Add toppings to an existing Pizza."""
        self.toppings += number_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new Pizza with existing Pizza's properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
