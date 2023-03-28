import tkinter
import time

CANVAS_HEIGHT = 100
CANVAS_WIDTH = 500

DX = -4
DY = 0
DELAY = 0.01

def get_messages():
    """
    Reads a series of messages from the user, ending when they
    input a blank message. Returns a list of all the messages 
    the user typed.
    """
    messages = []
    while True:
        msg = input("Type a message here or press enter to finish: ")
        if not msg:
            break
        messages.append(msg)
    return messages

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "News Ticker")
    
    messages = get_messages()
    index = 0
    text = canvas.create_text(
        CANVAS_WIDTH, 
        CANVAS_HEIGHT/2, 
        anchor='w', 
        fill='red', 
        text=messages[index], 
        font=('Calibri', 24)
    )

    while True:
        if get_right_x(canvas, text) < 0:
            index = (index+1) % len(messages)
            text = canvas.create_text(
                CANVAS_WIDTH, 
                CANVAS_HEIGHT/2, 
                anchor='w', 
                fill='red', 
                text=messages[index], 
                font=('Calibri', 24)
            )
        canvas.move(text, DX, DY)
        
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()


"""
You don't need to modify code below here
"""


def get_right_x(canvas, object):
    bbox = canvas.bbox(object)
    return bbox[2]


def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == "__main__":
    main()
