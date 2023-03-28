from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Checks every 4th column and repairs if needed until the end of the wall.
    """
    while front_is_clear():
        process_column()
        move_four_steps()
    process_column()

def process_column():
    """
    Checks the current column where the karel at and 
    fills in the column with beepers if there is 
    any beeper in the column.
    """
    turn_left()
    if beeper_exist_to_wall():
        move_to_wall()
        turn_around()
        put_beeper_to_wall()
    else:
        turn_around()
        move_to_wall()
    turn_left()

def beeper_exist_to_wall():
    """
    Moves karel to the end of the row/column and 
    returns true if there is any beeper on the way.
    """
    while front_is_clear():
        if beepers_present():
            return True
        move()
    return beepers_present()

def move_four_steps():
    """
    Moves karel 4 steps ahead.
    Stops if there is any wall ahead.
    """
    for i in range(4):
        if front_is_blocked():
            break
        move()

def move_to_wall():
    """
    Moves karel until the front is blocked.
    """
    while front_is_clear():
        move()

def put_beeper_to_wall():
    """
    Moves karel and put beepers on the way until the front is blocked.
    """
    while front_is_clear():
        put_beeper_one()
        move()
    put_beeper_one()

def put_beeper_one():
    """
    Puts a beeper in the current corner if there is no beeper existing.
    """
    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
