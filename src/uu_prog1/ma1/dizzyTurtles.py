# /src/uu_prog1/ma1/dizzyTurtles.py

#  import turtle
import random

#  from flags import jump
from flags import rectangle
from flags import make_turtle


def random_turtle(side=500, new_rectangle=True):
    half_side = side / 2
    if new_rectangle:
        rectangle(-half_side, -half_side, side, side, "cornsilk", "dark grey")
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


#  t = random_turtle(500)
#  for i in range(250):
#      move_random(t)

t = random_turtle()
t.color("dark blue")
u = random_turtle(new_rectangle=False)
u.color("red")
for _ in range(500):
    if t.distance(u) < 50:
        t.write("close")
    move_random(t)
    move_random(u)
