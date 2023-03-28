from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Fills the row with beepers where karel ends up in the middle of the row.
    Puts an additional beeper in the middle postion.
    Every corner in the row has 1 beeper except the middle one has 2.
    Clears each corner in the row by 1 beeper.
    The row ends up having only 1 beeper in the middle corner.
    """
    fill_line_middle()
    put_beeper()
    move_to_wall()
    turn_around()
    clear_line_one()
    turn_around()
    move_until_beeper()

def move_until_beeper():
    """
    Moves karel until there is a beeper in the karel's position.
    """
    while no_beepers_present():
        move()

def clear_line_one():
    """
    Clear one beeper at each corner in the line where karel is standing at, if any.
    Precondition: Behind karel is a wall.
    Postcondition: Karel at original position facing the same direction.
    """
    pick_a_beeper()
    while front_is_clear():
        move()
        pick_a_beeper()

def pick_a_beeper():
    """
    Pick one beeper at the current corner, if any.
    """
    if beepers_present():
        pick_beeper()

def fill_line_middle():
    """
    Fills line with beepers where karel currently staying at.
    Karel ends up being in the middle of the line. 
    """
    put_beeper()
    move_until_obstacle()
    while no_beepers_present():
        put_beeper()
        turn_around()
        move_until_obstacle()

def move_until_obstacle():
    """
    Moves karel until the front is blocked or there is a beeper in the corner ahead.
    """
    while front_is_clear():
        move()
        if beepers_present():
            move_back()
            break

def move_to_wall():
    """
    Moves karel until the front is blocked.
    """
    while front_is_clear():
        move()

def move_back():
    """
    Moves karel one step back, same direction as current position.
    """
    turn_around()
    move()
    turn_around()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
