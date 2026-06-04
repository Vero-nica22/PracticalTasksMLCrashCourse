###Veronica Morante Caicedo

# Introduction to Artificial Intelligence. Practical Tasks

## Task.1 Rock-Paper-Scissors

# The Rock-Paper-Scissors game is a simple hand game played between two players. It is often used as a decision-making tool or a playful way to make choices between two individuals. The game involves three hand shapes, each representing one of the three options: "rock," "paper," or "scissors." The rules are straightforward:

# 1. Rock crushes Scissors: Rock wins against Scissors.
# 2. Paper covers Rock: Paper wins against Rock.
# 3. Scissors cut Paper: Scissors win against Paper.

# The game follows a cyclic pattern, where each option beats one and loses to another. If both players choose the same option, the game results in a tie or draw.

# The Rock-Paper-Scissors game is typically played in a series of rounds. Each player makes their choice by forming one of the hand shapes (rock, paper, or scissors) simultaneously. Then, the choices are revealed, and the winner of the round is determined based on the rules above. The game continues until a predetermined number of rounds are completed, and the player with the most wins is declared the overall winner.
# """

# !pip install git+https://github.com/mehalyna/cooltest.git

from cooltest.test_cool_2 import *

"""Your task is to write the body of function `play_rock_paper_scissors()` in such a way that it would be used to play the game with the computer.

In this version of the function, the player's choice (from the user) and computer's choice (randomly generated) will be taken as input parameter. The winner is determined based on the **Rock-Paper-Scissors** game rules, and the result of the round is displayed. The user can play the game against the computer by providing their choice as input.
"""



@test_play_rock_paper_scissors
def play_rock_paper_scissors(player_choice, comp_choice):

    valid_choices = {'rock', 'paper', 'scissors'}
    if player_choice not in valid_choices or comp_choice not in valid_choices:
        return ("Invalid choice, Please choose'rock', 'paper', or 'scissors'.")

    if player_choice == comp_choice:
        result = "Tie"
    elif player_choice == 'rock' and comp_choice == 'scissors':
        result = "Player 1 wins"
    elif player_choice == 'paper' and comp_choice == 'rock':
        result = "Player 1 wins"
    elif player_choice == 'scissors' and comp_choice == 'paper':
        result = "Player 1 wins"
    else:
        result = "Comp wins"
    return result
play_rock_paper_scissors("paper", "rock")

"""Your next task is to write the body of function `computer_makes_choice` in such a way that it would return the choice of the computer.

The computer's choice will be randomly generated using the `random.choice()` function.
"""

import random

@ test_computer_makes_choice
def computer_makes_choice():
    """
    Generates the choise of the computer in the Rock-Paper-Scissors game.

    Parameters:
        none.

    Returns:
        str: The choice of the player. Should be one of 'rock', 'paper', or 'scissors'.

    Example:
        >>> computer_makes_choice()
        'rock'
        >>> computer_makes_choice()
        'scissors'
    """
    valid_choices = {'rock', 'paper', 'scissors'}

    # Generate computer's choice randomly

    result = random.choice(list(valid_choices))
    return result

computer_makes_choice()

"""Write the body of function `play_multiple_rounds(num_rounds)` that will directly call the `play_rock_paper_scissors()` function inside the loop for each round. The game proceeds as before, with the user inputting their choice, and the result of each round is displayed accordingly."""

def play_multiple_rounds(num_rounds):
    """
    Play multiple rounds of the Rock-Paper-Scissors game against the computer.

    Parameters:
        num_rounds (int): The number of rounds to play.

    Returns:
        None

    Example:
        >>> play_multiple_rounds(3)
        Enter your choice (rock/paper/scissors): rock
        Round 1: You chose rock. Computer chose paper. Comp wins

        Enter your choice (rock/paper/scissors): paper
        Round 2: You chose paper. Computer chose paper. Tie

        Enter your choice (rock/paper/scissors): scissors
        Round 3: You chose scissors. Computer chose rock. Comp wins
    """
    valid_choices = {'rock', 'paper', 'scissors'}
    print("---Play Rock Paper Scissors---")
    for round_num in range(1, num_rounds + 1):
        player_choice = input("Enter your choice rock, paper or scissors): ").lower()
        if player_choice not in valid_choices:
            print("Invalid choice, Please choose'rock', 'paper', or 'scissors'.")
            continue
        comp_choice = computer_makes_choice()
        result = play_rock_paper_scissors(player_choice, comp_choice)

    # Implementation of the dialog with the player
        print(f"Round {round_num}: You chose {player_choice}. Computer chose {comp_choice}. {result}")

    return None

# Example usage:
num_rounds = int(input("Enter the number of rounds to play: "))
play_multiple_rounds(num_rounds)

"""The simplicity and randomness of the Rock-Paper-Scissors game make it a popular choice for resolving disputes or making decisions in a fair and fun way.

## **Task 2. Hangman game**

Create a text-based version of the Hangman game. The computer selects a random word, and the player guesses letters until they solve the word or run out of attempts.

*Problem Definition:*

* You are tasked with implementing a simple Hangman game in Python.
* The game should select a random word from a predefined list of words.
* The player must guess letters in the word one at a time.
* If the player guesses a correct letter, it is revealed in the word.
* If the player guesses an incorrect letter, a part of the hangman is drawn.
* The player wins if they guess all the letters correctly before the hangman is fully drawn.
* The player loses if the hangman is fully drawn before they guess the word.
* The game should provide feedback to the player after each guess.
* The game continues until the player wins or loses.

Your Hangman game will consist of three functions: `select_random_word`, `display_word`, and `hangman_game`. The `hangman_game` function runs the game loop, while the other functions are used to select a random word and display the word with guessed letters filled in.

Certainly! Here's a description of each of the functions in the Hangman game:

1. `select_random_word` Function:

   This function is responsible for selecting a random word from a predefined list of words. It is used at the beginning of the game to choose the word that the player needs to guess.

   - Parameters: None
   - Returns: A randomly selected word (string).

2. `display_word` Function:

   This function takes two arguments: the target word to guess and a list of guessed letters. It generates a string where guessed letters are filled in, and unguessed letters are represented by underscores.

   - Parameters:
     - `word(str)`: The target word to guess.
     - `guessed_letters(list)`: List of letters guessed by the player.

   - Returns: The word with guessed letters filled in (string).


3. `hangman_game` Function:

   This function executes the Hangman game. It handles the game's main logic, including taking user input for letter guesses, checking if the guessed letters are correct, and displaying feedback to the player. The game continues until the player either wins by guessing the word correctly or loses by running out of attempts.

   - Parameters: None

Each function serves a specific role in the Hangman game, making the code modular and easier to understand. The `hangman_game` function ties everything together and provides the overall game experience for the player, including welcoming them, managing guesses, and announcing the game's outcome.
"""

import random

@test_select_random_word
def select_random_word():
    """
    Selects a random word from a predefined list of words.

    Returns:
    str: A randomly selected word.
    """
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "hamburger", "icecream", "jacket"]
    result = random.choice(word_list)
    return result

@test_display_word
def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters filled in and unguessed letters as underscores.

    Args:
    word (str): The target word to guess.
    guessed_letters (list): List of letters guessed by the player.

    Returns:
    str: The word with guessed letters filled in.
    """
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"

    return result

def hangman_game():
    """
    Executes the Hangman game.

    The player must guess letters in a randomly selected word until they either win or lose.
    """
    word_to_guess = select_random_word()
    guessed_letters = []
    max_attempts = 6  # Maximum attempts before losing

    print("Welcome to Hangman!")
    print("Try to guess the word. You can make up to 6 wrong guesses.")

    while max_attempts > 0:
        current_word = display_word(word_to_guess, guessed_letters)
        print(f"Word to guess: {current_word}")
        print(f"Attempts left: {max_attempts}")
        if "_" not in current_word:
            print("Congratulations! You Win :D")
            return
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)
        if guess not in word_to_guess:
            max_attempts -= 1
            print("Incorrect guess")
        else:
            print("Correct guess")
    print("Game Over")
    print("The word was:", word_to_guess)
    return None



# To play the game, call the hangman_game() function:

hangman_game()