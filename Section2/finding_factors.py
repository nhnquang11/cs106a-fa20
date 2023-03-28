SENTINEL = 0

def main():
	while True:
		number = int(input("Your number: "))
		if number == 0:
			break
		elif number < 0:
			print("Please input a positive number")
		else:
			find_factors(number)

def find_factors(n):
	for i in range(1, n+1):
		if n % i == 0:
			print(i)

if __name__ == "__main__":
	main()
	