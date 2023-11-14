"""This code will create a picture of a house using turtle objects."""
 
__author__ = "730710742"
 
from turtle import Turtle, done 
 
 
def main() -> None:
    """The entrypoint of my scene."""
    turt: Turtle = Turtle()
    draw_house(turt, -10, 5, 150, "Yellow", "Red")
    draw_windows(turt, 15, 50, 35, 20, "Blue")
    draw_windows(turt, 95, 50, 35, 20, "Blue")
    draw_windows(turt, 15, 125, 35, 20, "Blue")
    draw_windows(turt, 55, 125, 35, 20, "Blue")
    draw_windows(turt, 95, 125, 35, 20, "Blue")
    draw_door(turt, 55, 45, 40, 25, "Brown")
    draw_roof(turt, -15, 150, 165, "Brown", "Red")
    done()
 

def draw_house(turtle_var: Turtle, x: float, y: float, length: float, color_fill: str, outline_color: str) -> None:
    """This code will draw the base structure for the house which is essentially a square of given length with an outline and fill color that are also specified by the user."""
    turtle_var.penup()
    turtle_var.goto(x, y)
    turtle_var.setheading(0.0)
    turtle_var.pendown()
    turtle_var.color(outline_color, color_fill)
    turtle_var.begin_fill()
    index: int = 0
    while index < 4:
        turtle_var.forward(length)
        turtle_var.left(90)
        index = index + 1
    turtle_var.end_fill()


def draw_windows(turtle_var: Turtle, x: float, y: float, length: float, width: float, outline_color: str) -> None:
    """This code consists of building the windows for the house. These windows will be rectangulr and also have a unique outline color."""
    turtle_var.penup()
    turtle_var.goto(x, y)
    turtle_var.setheading(0.0)
    turtle_var.pendown()
    index: int = 0
    turtle_var.pencolor(outline_color)
    while index < 2:
        turtle_var.forward(width)
        turtle_var.right(90)
        turtle_var.forward(length)
        turtle_var.right(90)
        index = index + 1


def draw_door(turtle_var: Turtle, x: float, y: float, length: float, width: float, outline_color: str) -> None:
    """This code will create the door for the house which will be a rectangle with a cross going through it to add some design to the door."""
    turtle_var.penup()
    turtle_var.goto(x, y)
    turtle_var.setheading(0.0)
    turtle_var.pendown()
    index: int = 0
    turtle_var.pencolor(outline_color)
    turtle_var.goto(int(x + (width / 2)), y)
    turtle_var.setheading(270.0)
    turtle_var.forward(length)
    turtle_var.penup()
    turtle_var.goto(x, int(y - (length / 2)))
    turtle_var.pendown()
    turtle_var.setheading(0.0)
    turtle_var.forward(width)
    turtle_var.penup()
    turtle_var.goto(x, y)
    turtle_var.pendown()
    while index < 2:
        turtle_var.forward(width)
        turtle_var.right(90)
        turtle_var.forward(length)
        turtle_var.right(90)
        index = index + 1
    

def draw_roof(turtle_var: Turtle, x: float, y: float, length: float, outline_color: str, fill_color: str) -> None:
    """This codes the roof of the house which will be a triangle with a unique fill and outline color."""
    turtle_var.penup()
    turtle_var.goto(x, y)
    turtle_var.setheading(0.0)
    turtle_var.pendown()
    turtle_var.begin_fill()
    turtle_var.color(outline_color, fill_color)
    turtle_var.forward(length)
    turtle_var.left(120)
    turtle_var.forward(length)
    turtle_var.left(120)
    turtle_var.forward(length)
    turtle_var.end_fill()


if __name__ == "__main__":
    main()