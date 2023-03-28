"""
File: khansole_academy.py
-------------------------
The program randomly generates simple addition problems for the user,
reads in the answer from the user, and then checks to see if
they for it right or wrong, until the user appears to have mastered the material.
"""

import random

WIN_STREAK = 3
MIN_RANDOM = 10
MAX_RANDOM = 99

def main():
    streak = 0
    while streak < WIN_STREAK:
        a = random.randint(MIN_RANDOM, MAX_RANDOM)
        b = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(f"What is {a} + {b}?")
        user_answer = int(input("Your answer: "))
        total = a + b
        if user_answer == total:
            streak += 1
            print(f"Correct! You've gotten {streak} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {total}")
            streak = 0
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
