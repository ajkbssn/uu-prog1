# /src/uu_prog1/ma1/dizzyTurtles.py
"""
functions to move turtles randomly
script to draw square and follow turtles
"""

#  import turtle
import random

#  from flags import jump
from uu_prog1.flags import rectangle
from uu_prog1.flags import make_turtle


def random_turtle(side=500, draw_square=True):
    """return a turtle with random direction within a square, square can be drawn or not"""
    half_side = side / 2
    if draw_square:
        rectangle(
            -half_side,
            -half_side,
            side,
            side,
            fill_color="cornsilk",
            line_color="dark grey",
        )
    start_pos_x = random.randint(-half_side, half_side)
    start_pos_y = random.randint(-half_side, half_side)
    t = make_turtle(start_pos_x, start_pos_y)
    t.setheading(random.randint(0, 359))
    return t


def move_random(t):
    direction = t.heading()
    left = direction + 45
    right = direction - 45
    t.setheading(random.randint(right, left))
    t.forward(random.randint(0, 25))


def main():
    #  t = random_turtle(500)
    #  for i in range(250):
    #      move_random(t)

    t = random_turtle(draw_square=True)
    t.color("dark blue")
    u = random_turtle(draw_square=False)
    u.color("red")
    for _ in range(500):
        if t.distance(u) < 50:
            t.write("close")
        move_random(t)
        move_random(u)
        if abs(u.xcor()) >= 250 or abs(u.ycor()) >= 250:
            u.towards(0, 0)
        if abs(t.xcor()) >= 250 or abs(t.ycor()) >= 250:
            t.towards(0, 0)


if __name__ == "__main__":
    main()
