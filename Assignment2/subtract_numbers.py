"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The result is {a - b}.")

if __name__ == '__main__':
    main()
