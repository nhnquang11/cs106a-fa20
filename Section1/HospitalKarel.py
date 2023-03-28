from karel.stanfordkarel import *


def main():
   while front_is_clear():
      # build a hospital if a marker exists in karel's position
      if beepers_present():
         build_hospital()

      if front_is_clear():
         move()   

def build_hospital():
   """
   Builds a hospital in current position.
   """
   # get the marker and back up to build left column
   pick_beeper()
   back_up()
   build_sided_column()

   # move to next column to build middle column
   move()
   build_middle_column()

   # move to next column to build right column
   move()
   build_sided_column()

def build_sided_column():
   """
   Builds a height-3 column with the base is the current position.
   """
   turn_left()
   place_three_beepers()
   turn_around()
   move_to_wall()
   turn_left()

def build_middle_column():
   """
   Builds a height-3 column with the base is the top of the current position.
   """
   turn_left()
   move()
   place_three_beepers()
   turn_around()
   move_to_wall()
   turn_left()

def place_three_beepers():
   for i in range(3):
      put_beeper()
      move()

def move_to_wall():
   while front_is_clear():
      move()

def back_up():
   """
   Moves back karel 1 position facing the same orientation as current position.
   """
   turn_around()
   move()
   turn_around()

def turn_right():
   for i in range(3):
      turn_left()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
