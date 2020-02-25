import random
import time
import os

#function to clear the screen on windows or linux
def cls():os.system('cls' if os.name=='nt' else 'clear')

guessed_characters = []
lives = 7

cls()
#Welcome message
print('SHALL WE PLAY A GAME....')
time.sleep(1)
print('....OF HANGMAN' + '\n')
time.sleep(1)
print('I''M THINKING OF A WORD...' + '\n')
time.sleep(2)

def generate_guess_word():
    #hardcoded selection of number between  1 and 100
    random_int = random.randint(0,99)
    #open the list of provided words and use random number generated above to select random word
    word_list_doc = open("word_list.txt")
    word_list = word_list_doc.readlines()
    guess_word = word_list[random_int]
    return guess_word

def test_guesses(guessed_characters, guess_word):
    new_guess_word = []
    for i in guess_word:
        if i in guessed_characters:
            new_guess_word.append(i)
        else:
            new_guess_word.append('*')
    _guess_word = ''.join(new_guess_word)
    _guess_word = _guess_word[:-1]

    return _guess_word

def calculate_lives_remaining(guessed_characters, guess_word):
    global lives
    is_correct_guess = False
    if guessed_characters[-1] in guess_word:
        is_correct_guess = True
    else:
        lives -= 1
    return lives

def display_guessed_characters(guessed_characters):
    print("Letters you've tried already: " + str(guessed_characters) + '\n')

guess_word = list(generate_guess_word())
answer = ''.join(guess_word)
print(test_guesses(guessed_characters, guess_word))

while lives != 0:
    guessed_characters.append(str(input('Please Enter Your Next Guess: ').lower())) #adds lowercase version of input to guessed character list
    result = test_guesses(guessed_characters, guess_word)
    display_guessed_characters(guessed_characters)
    lives = calculate_lives_remaining(guessed_characters, guess_word)
    print('Number of Lives Remaining: ' + str(lives) + '\n')
    print(result)

    if not '*' in result:
        print("Congratulations you win")
        break

if lives == 0:
    print("You Lose" + '\n')
    print("The correct answer was: " + answer)
    time.sleep(1)
    print("HOW ABOUT A NICE GAME OF CHESS?")