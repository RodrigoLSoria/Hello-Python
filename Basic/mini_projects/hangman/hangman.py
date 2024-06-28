import random 
from words_list import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # gwtting user input
    while len(word_letters) > 0:
        #letters used
        print('You have', lives, 'lives and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('letter is not in the word')

        elif user_letter in used_letters:
            print("You have already used that character, please try another one.")
        else:
            print('Invalid character, please try again')

    # gets here when lives == 0 or  len(word_letters) == 0
    if lives == 0:
        print('you died, sorry. The word was ', word)
    else:
        print('you guess the word ', word, ', congratulations!!')


    
hangman()