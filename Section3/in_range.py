
def in_range(n, low, high):
	"""
	>>> in_range(2, 1, 3)
	True 
	>>> in_range(2, 3, 1)
	False
	>>> in_range(1, 1, 1)
	True
	"""
	return low <= n <= high


def main():
	a = int(input("Enter the first number: "))
	b = int(input("Enter the second number: "))
	c = int(input("Enter the third number: "))
	if in_range(b, min(a, c), max(a, c)):
		print(f"{b} is in between {a} and {c}")
	else:
		print(f"{b} is not in between {a} and {c}")

if __name__ == "__main__":
	main()
