from random import choice

from functions import current_draw
from functions import modify_current
from functions import check_is_correct
from functions import loading

from constants import word_diz

# Intro
print('HANGMAN by ezan')
current_draw(6)

# Set word
while True:
    print('> Names\n> Cities\n> Things\n> Animals\n> Colors')
    key = input('Choose a topic: ').lower().strip()
    if key in word_diz:
        break
    else:
        print('Choose a CORRECT topic!')
        continue

          
# Main variables
errors = 0
already_used = []
word_to_guess = choice(word_diz[key])
current_word = '_ ' * len(word_to_guess)

print(f'\n===> TOPIC: {key}', end='')
loading()

# Game starts
print(f'=========================')
print('\n   ==== GAME STARTS ====\n')

# Game loop
while True:
    # Current situation
    print('==========================')
    print(f'\n===> TOPIC: {key}')
    current_draw(errors)
    print(current_word+'\n')
    print(f'Letters used: {already_used}')
    
    # Stop game (if max errors or correct word)
    if errors == 6 or word_to_guess == current_word.replace(' ', ''):
        break
    
    # Try a letter
    try_letter = input('Choose a letter: ').lower().strip()
    
    # Correct input
    if check_is_correct(try_letter, already_used):
        
        # Wrong letter
        if try_letter not in word_to_guess:
            print('Wrong letter, try again', end='')
            errors += 1
            loading()
        
        # Correct letter
        else:
            print('Correct choice!', end='')
            current_word = modify_current(word_to_guess, try_letter, current_word)
            loading()
        
        # update list of letters
        already_used.append(try_letter)
    
    # Invalid input
    else:
        if not try_letter.isalpha() or len(try_letter) != 1:
            print('Invalid input, please enter a correct letter', end='')
        else:
            print('Already used, try again', end='')
            
        loading()
        continue
  
# Game Ends
print('\n==========================')
print('\n   ==== GAME ENDS ====\n')
print('==========================\n')
if errors == 6:
    print('You LOST...')
   
else:
    print('Congrats! You WON!')

print(f'Total errors: {errors}')
print(f'Total letters used: {already_used}')
         
        
        
    

