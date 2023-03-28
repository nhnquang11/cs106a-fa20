"""
File: word_guess.py
-------------------
Hangman game.
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    char_list = ['-' for i in range(len(secret_word))]
    num_guesses = INITIAL_GUESSES
    guessed_chars = set()
    game_over = False
    while not game_over:
        print(f"The word now looks like this: {''.join(char_list)}")
        print(f"You have {num_guesses} left.")
        char = input("Type a single letter here, then press enter: ").upper()
        if not is_valid(char):
            print("Guess should only be a single character.")
        elif char in guessed_chars:
            print(f"The character {char} has been guessed before. Try again!")
        else:
            guessed_chars.add(char)
            if char in secret_word:
                update(char_list, secret_word, char)
                print("That guess is correct.")
                if ''.join(char_list) == secret_word:
                    print(f"Congratulations, the word is: {secret_word}")
                    game_over = True
            else:
                num_guesses -= 1
                print(f"There are no {char}'s in the word")
                if num_guesses == 0:
                    print(f"Sorry, you lost. The secret word was: {secret_word}")
                    game_over = True

def is_valid(guess):
    return len(guess) == 1

def update(char_list, secret_word, char):
    for i in range(len(char_list)):
        if secret_word[i] == char:
            char_list[i] = char

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    lexicon_list = []
    with open(LEXICON_FILE) as file:
        for word in file:
            lexicon_list.append(word.strip())
    return random.choice(lexicon_list)

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()