from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    # Move to the newspaper
    go_outside()

    # Pick the newspaper up
    pick_beeper()

    # Return to karel's starting point
    get_back()

def go_outside():
    """
    Moves karel outside the door.
    Precondition: Northwest corner of the house, facing west.
    Postcondition: Outside the door, facing west.
    """
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()

def get_back():
    """
    Moves karel back to the original position.
    Precondition: Outside the door, facing west.
    Postcondition: Northwest corner of the house, facing west.
    """
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
