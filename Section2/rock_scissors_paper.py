from random import randint

def main():
	rounds_won = 0
	print("1 - rock")
	print("2 - scissors")
	print("3 - paper")
	for i in range(5):
		human_choice = int(input("Your move (1, 2, or 3): "))
		if play(human_choice):
			rounds_won += 1
	print("You won " + str(rounds_won) + " rounds!")

def play(human_choice):
	computer_choice = randint(1, 3)
	if human_choice == computer_choice:
		print("It's a tie!")
		return False
	else:
		if human_choice == 1: # rock
			if computer_choice == 2: # scissors
				print("You Win! Rock crushes scissors")
				return True
			elif computer_choice == 3: # paper
				print("You Lose! Paper covers rock")
				return False
		elif  human_choice == 2: # scissors
			if computer_choice == 1: # rock
				print("You Lose! Rock crushes scissors")
				return False
			elif computer_choice == 3: # paper
				print("You Win! Scissors cuts paper")
				return True
		elif human_choice == 3: # paper
			if computer_choice == 1: # rock
				print("You Win! Paper covers rock")
				return True
			elif computer_choice == 2: # scissors
				print("You Lose! Scissors cuts paper")
				return False

if __name__ == "__main__":
	main()
