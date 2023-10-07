"""My attempt at Wordle."""
import random
import csv


__author__: str = "Somer Lillard"
"""CSV file from Bill Cruise on Kaggle: https://www.kaggle.com/datasets/bcruise/wordle-valid-words/data"""


def contains_char(word: str, one: str) -> bool:
    """Checks the characters in any word for matches."""
    assert len(one) == 1
    i: int = 0
    while i < len(word):
        if word[i] == one:
            i += 1
            return True
        else:
            i += 1
    return False


# values for my emoji strings
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Emojifying my secret word guess."""
    assert len(guess) == len(secret)
    i2: int = 0
    emojis: str = ""
    while i2 < len(guess):
        if guess[i2] == secret[i2]:
            emojis += GREEN_BOX
        else:
            if contains_char(secret, guess[i2]) is True:
                emojis += YELLOW_BOX
            else:
                emojis += WHITE_BOX
        i2 += 1
    return emojis


def input_guess(expected_length: int) -> str:
    """Making the user input a guess of correct length."""
    guessed_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guessed_word) != expected_length:
        guessed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_word

# choosing a random word for wordle
def choose_random_word_from_csv():
    try:
        with open("valid_solutions.csv", 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            # Skip the header row if it exists
            next(csv_reader, None)
            # Collect all the words from the CSV file
            word_list = [row[0] for row in csv_reader]
            # Choose a random word from the list
            random_word = random.choice(word_list)
            return random_word
    except FileNotFoundError:
        return "File not found"

# main area of my game
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = choose_random_word_from_csv()
    turn_number: int = 1
    not_won = True
    while turn_number <= 6 and not_won:
        print(f"=== Turn {turn_number}/6 ===")
        game_guessed_word: str = input_guess(len(secret_word))
        emojis: str = emojified(game_guessed_word, secret_word)
        print(emojis)
        if game_guessed_word == secret_word:
            not_won = False
        else:
            turn_number += 1
    if not_won is False:
        print(f"You won in {turn_number}/6 turns!")
    if not_won is True:
        print("Turn X/6 - Sorry, try again tomorrow!")
        print("word was: " + secret_word)


# next lines used to be able to run this file as a module
if __name__ == "__main__":
    main()