# /src/uu_prog1/ma1/flags.py
"""functions to draw flags"""

import turtle


def make_turtle(x, y, visible=True):
    t = turtle.Turtle()
    if not visible:
        t.speed(0)
        t.hideturtle()
    jump(t, x, y)
    return t


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(x, y, width, height, fill_color="black", line_color="black"):
    t = make_turtle(x, y, visible=False)
    t.color(line_color, fill_color)
    t.begin_fill()
    for side in [width, height, width, height]:
        t.forward(side)
        t.left(90)
    t.end_fill()


def tricolore(x, y, h):
    """draw the French flag"""
    w = h / 2  # each rectangle width half height to get a 2:3 flag
    rectangle(x, y, w, h, fill_color="blue", line_color="")
    rectangle(x + w, y, w, h, "white", "light grey")
    rectangle(x + 2 * w, y, w, h, "red", "")


def pentagram_v1(x, y, side):
    """draw a five-point star, retired version"""
    t = make_turtle(x, y)
    t.hideturtle()
    t.right(72)
    for i in range(5):
        t.forward(side)
        t.right(144)


def pentagram(x, y, side, fill_type=None, fill_color="black", line_color="black"):
    """
    draw a five-point star,
    three fill types supported: "full", "outer" or None
    """
    t = make_turtle(x, y, visible=False)
    t.color(line_color, fill_color)
    t.right(72)
    if fill_type == "full":
        # maths from https://mathworld.wolfram.com/Pentagram.html
        edge = side * 2 / (5 + 5 ** 0.5)
        t.begin_fill()
        for i in range(5):
            t.forward(edge)
            t.left(72)
            t.forward(edge)
            t.right(144)
        t.end_fill()
    elif fill_type is None or fill_type == "outer":
        if fill_type == "outer":
            t.begin_fill()
        for i in range(5):
            t.forward(side)
            t.right(144)
        if fill_type == "outer":
            t.end_fill()
    else:
        pass  # raise an error?


def french_flag_with_stars(x, y, height):
    tricolore(x, y, height)
    for i in range(2):
        for j in range(5):
            pentagram(
                x - height / 4 + j * 0.5 * height,
                y - 0.1 * height + i * 1.51 * height,
                0.31 * height,
                fill_type="outer",
                fill_color="dark green",
                line_color="",
            )


def vietnamese_flag(x, y, height):
    # official colors red and yellow with hex representation
    viet_red = "#da251d"
    viet_yel = "#ffff00"
    rectangle(x, y, 1.5 * height, height, fill_color=viet_red, line_color="")
    # specs from https://en.wikipedia.org/wiki/Flag_of_Vietnam
    x_star = x + 0.8 * height
    y_star = y + 0.75 * height
    # maths from https://mathworld.wolfram.com/Pentagram.html
    side = height * 6 / 10 * (10 ** (1 / 2) / (5 + 5 ** (1 / 2)) ** (1 / 2))
    pentagram(
        x_star, y_star, side, fill_type="full", fill_color=viet_yel, line_color=""
    )


def main():
    """Assignment 1 & 2, lesson 5, Computer Programming I, UU, fall 2020"""
    french_flag_with_stars(0, 0, 200)
    vietnamese_flag(-400, -400, 200)
