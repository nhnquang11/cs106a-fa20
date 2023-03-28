from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Fills the first row before going in to loop to handle the fencepost problem.
    """
    fill_row_odd()
    while left_is_clear():
        go_next_row()
        fill_row_even()
        if left_is_clear():
            go_next_row()
            fill_row_odd()

def go_next_row():
    """
    Moves karel to the next row, same orientation as current position.
    """
    turn_left()
    move()
    turn_right()

def fill_row_odd():
    """
    Fill row with beepers start from the first position in the row.
    """
    fill_beepers()
    turn_around()
    move_to_wall()
    turn_around()

def fill_row_even():
    """
    Fill row with beepers start from the second position in the row.
    """
    if front_is_clear():
        move()
        fill_row_odd()

def fill_beepers():
    """
    From current position and orientation, 
    fills beepers on the current line.
    One space apart each beeper.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def move_to_wall():
    """
    Moves karel until the front is blocked.
    """
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
