from random import choice

from functions import current_draw
from functions import modify_current
from functions import check_word
from functions import check_letter
from functions import loading
from functions import power_strip

from constants import word_diz

# Intro
print('\nHANGMAN by ezan')
current_draw(6)

# Set word
while True:
    print('> Names\n> Cities\n> Things\n> Animals\n> Colors')
    key = input('Choose a topic: ').lower().strip()
    if key in word_diz:
        break
    else:
        print('\n!-------------------------!')
        print('  Choose a CORRECT topic!')
        print('!-------------------------!\n')
        continue

          
# Main variables
errors = 0
words_used = []
letters_used = []

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
    if words_used: print(f'Words used: {words_used}')
    if letters_used: print(f'Letters used: {letters_used}')
    
    # Stop game (if max errors or correct word)
    if errors == 6 or word_to_guess == current_word.replace(' ', ''):
        break
    
    # choose action
    while True:
        print('Do you want to guess the word? (2 Errors if wrong)')
        print('\t> type y if you want to guess the word\n\t> type n if you want to choose a letter\n')
        action = input('Your choice: ').lower().strip()
        if action not in 'yn':
            print('\n!------------------------------------!')
            print('  Invalid input, please enter y or n')
            print('!------------------------------------!')
            continue
        break
    
    if action == 'y':
        # Try a word
        try_word = power_strip(input('Enter your guess: ').lower())
        
        if check_word(try_word, words_used):
            
            # Correct word
            if try_word == word_to_guess:
                print('Correct choice!')
                loading()
                break
            
            # Wrong Word
            else:
                print('Wrong word, try again', end='')
                errors += 2
                # update list of words
                words_used.append(try_word)
                loading()
                
        # Invalid input
        else:
            if not try_word.isalpha():
                print('Invalid input, please enter a correct word', end='')
                
            else:
                print('Already used, try again', end='')
            
            loading()
                
                
    else:
        # Try a letter
        try_letter = input('Choose a letter: ').lower().strip()
        
        # Correct input
        if check_letter(try_letter, letters_used):
            
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
            letters_used.append(try_letter)
        
        # Invalid input
        else:
            if not try_letter.isalpha() or len(try_letter) != 1:
                print('Invalid input, please enter a correct letter', end='')
            else:
                print('Already used, try again', end='')
                
            loading()
            
  
# Game Ends
print('\n==========================')
print('\n   ==== GAME ENDS ====\n')
print('==========================\n')

print(f'CORRECT WORD: {word_to_guess.upper()}\n')
if errors == 6:
    print('You LOST...')
   
else:
    print('Congrats! You WON!')

print(f'[TOTAL] errors: {errors}')
if letters_used: print(f'[TOTAL] letters used: {letters_used}')
if words_used: print(f'[TOTAL] words used: {words_used}')
         
        
        
    

