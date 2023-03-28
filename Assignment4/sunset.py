"""
File: sunset.py
----------------
Stanford CS106A Sunset Project
This program animates scene of the setting sun.
"""

import tkinter
import time
from graphics import Canvas

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels
SUN_SIZE = 70           # Width and height of the sun oval

# The sun turns orange when the middle of the sun passes this y location
ORANGE_Y = CANVAS_HEIGHT * (1/3)
# The sun turns red when the middle of the sun passes this y location
RED_Y = CANVAS_HEIGHT * (2/3)

DX = 0 
DY = 1
DELAY = 1/50

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Sunset')

    sky = canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="blue")
    sun = canvas.create_oval(
        CANVAS_WIDTH / 2 - SUN_SIZE / 2,
        0,
        CANVAS_WIDTH / 2 + SUN_SIZE / 2,
        SUN_SIZE,
        outline="yellow",
        fill="yellow"
    )

    while get_top_y(canvas, sun) < CANVAS_HEIGHT:
        sun_y0 = get_top_y(canvas, sun)
        sun_color = get_sun_color(sun_y0)
        canvas.itemconfig(
            sun, 
            fill=sun_color, 
            outline=sun_color
        )
        canvas.move(sun, DX, DY)
        canvas.update()
        time.sleep(DELAY)
    
    print("animation complete")
    canvas.mainloop()

def get_top_y(canvas, obj):
    """
    Return the y0 coordinate of the object in the canvas.
    """
    return canvas.coords(obj)[1]

def get_sun_color(top_y):
    """
    Returns the sun color given the top position of the sun.
    """
    if top_y + SUN_SIZE/2 < ORANGE_Y:
        return "yellow"
    elif top_y + SUN_SIZE/2 < RED_Y:
        return "orange"
    else:
        return "red"

if __name__ == '__main__':
    main()
