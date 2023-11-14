"""Installing A Class!"""

from lessons.classes.pizza import Pizza

#Import the class
#From <file_name>.<module_name> import <class_name>
my_pizza: Pizza = Pizza("large", 10, True) #CONSTRUCTOR can assign arguments in here

#acessing/setting attributes
#my_pizza.size = "medium"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

#Printing out some valuesx
# print("my_pizza: ")
# print(my_pizza)

# print("Pizza: ")
# print(Pizza)

print("Size Attribute: ")
print(my_pizza.size)

print("Toppings: ")
print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Calculate price of Pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else: 
        price: float = 5.00
    price += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

#Calling function
print(price(sals_pizza))
print(price(my_pizza))

#Calling method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza)
print(my_pizza.toppings)