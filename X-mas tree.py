from turtle import Turtle, Screen
from random import randint

BG_COLOR = "midnight blue"
TREE_COLOR = "forest green"
TRUNK_COLOR = "saddle brown"
ORNAMENT_COLORS = ["red", "gold", "orange", "blue", "white"]
SNOW_COLOR = "snow"
TWINKLE_LIGHT_COLORS = ["red", "gold", "white", "yellow"]
STAR_COLOR = "gold"

def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()

def create_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def create_star(turtle, x, y, size):
    turtle.penup()
    turtle.color(STAR_COLOR)
    turtle.goto(x, y)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_christmas_tree(turtle, screen):
    # Draw snowy ground
    turtle.color(SNOW_COLOR)
    turtle.begin_fill()
    turtle.goto(-screen.window_width() // 2, -screen.window_height() // 2)
    for _ in range(2):
        turtle.forward(screen.window_width())
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    # Draw tree trunk
    create_rectangle(turtle, TRUNK_COLOR, -15, -50, 30, 60)

    # Draw tree layers
    width = 240
    turtle.speed(20)
    while width > 10:
        width -= 10
        height = 15  # Adjusted height for better proportions
        x = 0 - width / 2
        create_rectangle(turtle, TREE_COLOR, x, -30, width, height)

    # Draw decorations
    turtle.speed(1)
    turtle.penup()
    for x, y, color in [(-20, -10, "yellow"), (20, 40, "yellow"), (-40, 0, "red"),
                        (30, -40, "orange"), (85, -90, "white"), (-30, -50, "blue"), (-100, -110, "yellow")]:
        create_circle(turtle, x, y, 10, color)

    # Draw tree top star
    create_star(turtle, 0, 120, 25)

def draw_twinkle_lights(turtle, num_lights):
    turtle.speed(10)
    for _ in range(num_lights):
        x_light = randint(-(turtle.window_width() // 2), turtle.window_width() // 2)
        y_light = randint(-50, turtle.window_height() // 2)
        size = randint(5, 15)
        color = TWINKLE_LIGHT_COLORS[randint(0, len(TWINKLE_LIGHT_COLORS) - 1)]
        create_circle(turtle, x_light, y_light, size, color)

def falling_snow(turtle, num_snowflakes):
    turtle.speed(1)
    turtle.hideturtle()
    turtle.penup()
    turtle.color(SNOW_COLOR)

    for _ in range(num_snowflakes):
        x_snowflake = randint(-(turtle.window_width() // 2), turtle.window_width() // 2)
        y_snowflake = randint(0, turtle.window_height() // 2)
        size = randint(5, 15)
        turtle.goto(x_snowflake, y_snowflake)
        turtle.dot(size)

def main():
    christmasTree = Turtle()
    screen = Screen()
    screen.bgcolor(BG_COLOR)
    screen.title("Professional Christmas Scene")

    draw_christmas_tree(christmasTree, screen)

    # Add twinkling lights
    draw_twinkle_lights(christmasTree, 30)

    # Add falling snow
    falling_snow(christmasTree, 100)

    # Display festive message
    christmasTree.penup()
    christmasTree.color("white")
    christmasTree.goto(0, -200)
    christmasTree.write("MERRY CHRISTMAS", align="center", font=("Arial", 30, "bold"))

    screen.exitonclick()

if __name__ == "__main__":
    main()
