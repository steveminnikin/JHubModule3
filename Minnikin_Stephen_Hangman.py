import random
import time

guessed_characters = []

#Welcome message
print('WOULD YOU LIKE TO PLAY A GAME........OF HANGMAN')

time.sleep(2)

print('I''M THINKING OF A WORD...')

time.sleep(2)

def generate_guess_word():
    #hardcoded selection of number between  1 and 100
    random_int = random.randint(0,99)

    #open the list of provided words and use random number generated above to select random word
    word_list_doc = open("word_list.txt")
    word_list = word_list_doc.readlines()
    guess_word = word_list[random_int]

    return guess_word

guess_word = generate_guess_word()

def hide_guess_word(guess_word):
    hidden_guess_word = list(guess_word)
    for i in range(len(hidden_guess_word) -1):
        hidden_guess_word[i] = '*'

    s = ''
    hidden_guess_word = s.join(hidden_guess_word)

    return hidden_guess_word

hidden_guess_word = hide_guess_word(guess_word)

print(hidden_guess_word)
print(guess_word)

def test_guesses(guessed_characters, guess_word):
    guess_word_list = list(guess_word)
    print(guess_word_list)
    for i in guessed_characters:
        print(i)
        for j in guess_word_list:
            if i != j:
                 j = '*'
            print(i + ',' + j)
        print(guess_word_list)

    s = ''
    guess_word = s.join(guess_word_list)

    return



guessed_characters.append(str(input('ENTER A GUESS: ')))

test_guesses(guessed_characters, guess_word)

#while guessed word != guess_word:
    
