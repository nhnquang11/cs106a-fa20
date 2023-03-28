DOG_YEARS_PER_HUMAN_YEAR = 7
SENTINEL = 0

def main():
	while True:
		human_age = int(input("Enter an age in human years: "))
		if human_age == 0:
			break
		elif human_age < 0:
			print("Sorry, please enter a positive number or 0 to exit")
		else:
			dog_age = human_age * DOG_YEARS_PER_HUMAN_YEAR
			print("The age in dog years is " + str(dog_age))

if __name__ == "__main__":
	main()
	