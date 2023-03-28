FILENAME = 'word.txt'

def create_word_list(filename):
	"""
	Return a list of word from filename directory.
	"""
	word_list = []
	with open(filename) as file:
		for word in file:
			word_list.append(word.strip())
	return word_list

def get_anagrams(word, word_list):
	"""
	Return a list of anagrams of the given word from the word list.
	"""
	return [w for w in word_list if check_anagram(word, w)]

def check_anagram(w1, w2):
	"""
	Check whether two words are anagrams or not.
	"""
	return sorted(w1) == sorted(w2)

def main():
	word_list = create_word_list(FILENAME)
	while True:
		word = input("Word: ")
		if word == '':
			break
		anagrams = get_anagrams(word, word_list)
		if not anagrams:
			print(f"{word} is not in the dictionary")
		else:
			print(anagrams)

if __name__ == '__main__':
	main()
