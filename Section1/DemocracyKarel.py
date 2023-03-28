from karel.stanfordkarel import *

def main():
    while front_is_clear():
        process_column()
        move()
    process_column()

def process_column():
    if no_beepers_present():
        remove_all_chads()

def remove_all_chads():
    """
    Clears chad from the current column, if any.
    """
    clear_top()
    clear_bottom()

def clear_top():
    """
    Clears chad from the top of current position, if any.
    """
    # go to the top and clear beepers
    turn_left()
    move()
    clear_chads()

    # get back to the original position
    turn_around()
    move()
    turn_left()

def clear_bottom():
    """
    Clears chad from the bottom of current position, if any.
    """
    # go to the bottom and clear beepers
    turn_right()
    move()
    clear_chads()

    # get back to the original position
    turn_around()
    move()
    turn_right()

def clear_chads():
    """
    Clear chads from the current position, if any.
    """
    while beepers_present():
        pick_beeper()

def turn_right():
    for i in range(3): 
        turn_left()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
