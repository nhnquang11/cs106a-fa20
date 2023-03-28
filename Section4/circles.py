import sys
import tkinter
import random

WIDTH = 800
HEIGHT = 600
RADIUS_MIN = 30
RADIUS_MAX = 100
N_CIRCLES_MAX = 10

def make_canvas():
    """
    (provided)
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=WIDTH + 10, height=HEIGHT + 10)

    canvas = tkinter.Canvas(top, width=WIDTH, height=HEIGHT)
    canvas.pack()
    canvas.xview_scroll(6, 'units')  # hack so (0, 0) works correctly
    canvas.yview_scroll(6, 'units')

    return canvas


def make_all_circles():
    canvas = make_canvas()

    num_circles = random.randint(1, N_CIRCLES_MAX)
    for i in range(num_circles):
        make_a_circle(canvas)

def make_a_circle(canvas):
    radius = random.randint(RADIUS_MIN, RADIUS_MAX)
    x0 = random.random() * (WIDTH - 2 * radius)
    y0 = random.random() * (HEIGHT- 2 * radius)
    x1 = x0 + 2 * radius
    y1 = y0 + 2 * radius
    canvas.create_oval(x0, y0, x1, y1)

def main():
    """
    random-circles.py
    Write a program that draws a random number of circles of random sizes at random positions on the canvas. Be careful to make sure that none of the drawn circles are cut off by the edge of your canvas. You are provided with the constants WIDTH/HEIGHT (the canvas width/height), RADIUS_MAX/RADIUS_MIN (the maximum/minimum radius that each random circle may have), and N_CIRCLES_MAX (the maximum number of circles that may be generated in one run of our program. Note that each run should generate between 1 and N_CIRCLES_MAX circles inclusive on both ends). 
    """
    make_all_circles()
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()
