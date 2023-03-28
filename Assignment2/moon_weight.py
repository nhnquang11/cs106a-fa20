"""
File: moon_weight.py
--------------------
This program calulates how much people would weigh if they were on the moon
based on their current weight on the earth.
"""

MOON_PCT = 0.165

def main():
    weight_on_earth = float(input("Enter your weight: "))
    if weight_on_earth < 0:
        print("Sorry, you can't have a negative weight.")
    else:
        weight_on_moon = weight_on_earth * MOON_PCT
        print(f"Your weight on the moon is {weight_on_moon}")

if __name__ == '__main__':
    main()
