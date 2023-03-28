def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    n = int(input("Number to count to: "))
    fizzbuzz(n)

if __name__ == "__main__":
    main()
