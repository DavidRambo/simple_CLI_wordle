"""
Simple Wordle Clone
wordle.py"""
import sys
import wordle_functions

# List of words
word_list = ['could', 'train', 'wired', 'angle', 'count', 'found', 'moist',
             'doubt', 'dread', 'bread', 'flame', 'skill']


def wordle_game():
    '''Main game loop'''
    turn_count = 0  # start turn count at zero

    # First, randomly generate a word to be guessed.
    # the_answer = wordle_functions.randomize_word(word_list)
    the_answer = "skill"

    # Now the game gets into its loop, which is controlled by two factors:
    # turn count and a correct guess.
    while turn_count < 6:
        # Ask for a guess word from the player.
        the_guess = wordle_functions.word_guess()

        # Check for correct answer.
        if the_guess == the_answer:
            sys.exit(f"You guessed it! {the_answer.upper()} is the word.")

        # Then check that guess against the answer.
        wordle_functions.improved_check_function(the_guess, the_answer)

        # Mark end of turn by advancing count by one and printing result.
        turn_count += 1

    print("You ran out of guesses. The word was:", the_answer.upper())


wordle_game()
