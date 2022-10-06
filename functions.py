from time import sleep

def current_draw(errors):
    with open(f'draws/file_{errors}.txt') as fr:
        draw = fr.read()
    print(draw+'\n')


def modify_current(word_to_guess, try_letter, current_word):
    index_list = []
    current_word = current_word.split()
    for i, letter in enumerate(word_to_guess):
        if try_letter == letter:
            index_list.append(i)
    for index in index_list:
        current_word[index] = try_letter
    return ' '.join(current_word)


def check_is_correct(letter, already_used):
    return letter.isalpha() and len(letter) == 1 and letter not in already_used

def loading():
    for p in '...':
        print(p, end='')
        sleep(0.5)
    print()
    print()
        
        