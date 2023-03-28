"""
File: hailstones.py
-------------------
Hailstones problem.
"""

def main():
    n = int(input("Enter a number: "))
    num_steps = 0
    while n != 1:
        if n % 2 == 1:
            print(f"{n} is odd, so I make 3n + 1: {3 * n + 1}")
            n = 3 * n + 1
        else:
            print(f"{n} is even, so I take half: {n // 2}")
            n = n // 2
        num_steps += 1
    print(f"The process took {num_steps} steps to reach 1")

if __name__ == '__main__':
    main()
