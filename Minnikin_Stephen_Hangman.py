import random
import time

#Welcome message
print('Welcome to Steve Minnikin''s JHub Module 3 Submission, Let''s play a game of hangman')

time.sleep(2)

print('I''m thinking of a word...')

time.sleep(2)

def generate_guess_word():
    #hardcoded selection of number between  1 and 100
    random_int = random.randint(0,99)

    #open the list of provided words and use random number generated above to select random word
    word_list_doc = open("word_list.txt")
    word_list = word_list_doc.readlines()
    guess_word = word_list[random_int]

    return guess_word

def hide_guess_word(guess_word: str):
    for c in enumerate(guess_word):
        c += '*'
    return guess_word

guess_word = generate_guess_word()

hidden_guess_word = hide_guess_word(guess_word)

print(hidden_guess_word)
