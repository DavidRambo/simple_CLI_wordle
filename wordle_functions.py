"""Functions to import for wordle.py game"""
import random


def randomize_word(list_of_words: list) -> str:
    '''Randomly select word to be the answer'''
    return random.choice(list_of_words)


def word_guess() -> str:
    '''Ask user to guess a word.'''
    # Ask user to guess a word and ensure it is all lowercase
    guess = input('Guess a five-letter word: ').lower()
    # Error handling stuff
    # guess = str()

    while len(guess) != 5 or not guess.isalpha():
        guess = input('Your word is not five letters long.\nGuess again: ')
    return guess.lower()


def improved_check_function(guess: str, answer: str) -> str:
    '''This should replicate Wordle's algorithm regarding duplicate letters'''
    result_letters = []
    result_positions = []
    display = []
    new_guess = []
    new_answer = []
    # Turn the strings into lists of their constiuent characters.
    guess_list = list(guess)
    answer_list = list(answer)

    for letter1, letter2 in zip(guess_list, answer_list):
        if letter1 == letter2:
            # can also put the if statement into append()
            # but I find that more difficult to read
            result_letters.append(letter1.upper())
            result_positions.append(guess_list.index(letter1))
            new_guess.append('?')
            new_answer.append('_')
        else:
            new_guess.append(letter1)
            new_answer.append(letter2)

    for letter in new_answer:
        if letter in new_guess:
            result_letters.append(letter)
            result_positions.append(new_guess.index(letter))

    for position in range(0, 5):
        if position in result_positions:
            display.append(result_letters[result_positions.index(position)])
        else:
            display.append('_')

    # return as string by joining the separate items in the list,
    # separating each letter with a space (that's the ' ').
    print(' '.join(display))
