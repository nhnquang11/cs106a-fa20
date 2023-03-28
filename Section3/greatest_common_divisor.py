
def greatest_common_divisor(a, b):
    """
    Return the greatest common divisor of a and b.

    >>> greatest_common_divisor(4, 16)
    4
    >>> greatest_common_divisor(16, 4)
    4
    >>> greatest_common_divisor(9, 24)
    3
    """
    lower = min(a, b)

    gcd = 1
    for i in range(1, lower+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def main():
    num_1 = int(input("num 1: "))
    num_2 = int(input("num 2: "))
    print(greatest_common_divisor(num_1, num_2))
