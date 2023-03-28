def is_palindrome(word):
	"""
	Checks whether the given word is a palindrome or not.
	>>> is_palindrome("Racecar")
	True
	>>> is_palindrome("Kayak")
	True
	>>> is_palindrome("Dog")
	False
	"""
	word = word.lower()
	return word == word[::-1]

def is_tridrome(word):
	"""
	Checks whether the given word is a tridrome or not.
	A word is a tridrome if it has at least 6 characters and 
	the first three letters of the word are the same as the last three letters of the word.
	>>> is_tridrome('Underground')
	True
	>>> is_tridrome('Entertainment')
	True
	>>> is_tridrome('Murmur')
	True
	>>> is_tridrome('Cat')
	False
	>>> is_tridrome('Perplexing')
	False
	"""
	if len(word) < 6:
		return False
	word = word.lower()
	return word[:3] == word[-3:]

def is_peaceful(word):
	"""
	Checks whether a given word is 'peaceful' or not.
	A word is peaceful if its letters are in alphabetical order.
	>>> is_peaceful('Almost')
	True
	>>> is_peaceful('Chips')
	True
	>>> is_peaceful('Dirty')
	True
	>>> is_peaceful('Zebra')
	False
	>>> is_peaceful('A')
	True
	"""
	word = word.lower()
	for i in range(len(word)):
		if i == len(word) - 1:
			return True
		if word[i] > word[i+1]:
			return False
	return True

def is_stacatto(word):
	"""
	Checks whether a word is a stacatto or not.
	A word is a stacatto if all of the letters in the even positions are vowels.
	>>> is_stacatto('Automatic')
	True
	>>> is_stacatto('Cafeteria')
	True
	>>> is_stacatto('Hesitate')
	True
	>>> is_stacatto('Hi')
	True
	>>> is_stacatto('H')
	True
	>>> is_stacatto('Shift')
	False
	"""
	word = word.lower()
	if len(word) == 1:
		return True
	for char in word[1::2]:
		if char not in 'aeiouy':
			return False
	return True

def count_tridromes(filename):
	"""
	Returns the number of tridromes in the given file.
	"""
	counter = 0
	with open(filename) as file:
		for word in file:
			word = word.strip()
			if is_tridrome(word):
				counter += 1
	return counter

def count_peaceful(filename):
	"""
	Returns the number of peaceful words in the given file.
	"""
	counter = 0
	with open(filename) as file:
		for word in file:
			word = word.strip()
			if is_peaceful(word):
				counter += 1
	return counter

def count_stacatto(filename):
	"""
	Returns the number of stacatto in the given file.
	"""
	counter = 0
	with open(filename) as file:
		for word in file:
			word = word.strip()
			if is_stacatto(word):
				counter += 1
	return counter

def count_words(filename):
	"""
	Returns the total number of words in the given file.
	"""
	counter = 0
	with open(filename) as file:
		for line in file:
			counter += 1
	return counter

def main():
	filename = "word.txt"
	print(f"Out of {count_words(filename)} words in total: ")
	print(f"The file has {count_tridromes(filename)} tridromes.")
	print(f"The file has {count_peaceful(filename)} peaceful words.")
	print(f"The file has {count_stacatto(filename)} stacattos.")

if __name__ == '__main__':
	main()
