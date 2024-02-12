from random import randint
from math import ceil
import requests
import os

# Clear the screen
os.system('cls')

# Prompt user to select difficulty level
print("\nSelect your difficulty level")
print("\t1. n00b")
print("\t2. ez")
print("\t3. player fr")
print("\t4. G.O.A.T")
print("\t5. Asian")
difficulty = int(input("Enter selection: "))

# Assign word length based on selected difficulty
if difficulty == 1:
    word_len = 5
if difficulty == 2:
    word_len = randint(5, 7)
if difficulty == 3:
    word_len = randint(8, 10)
if difficulty == 4:
    word_len = randint(10, 15)
if difficulty == 5:
    word_len = 15

# Fetch a random word of the selected length
url = f"https://random-word-api.herokuapp.com/word?length={word_len}"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    word_to_guess = data[0]

# Initialize variables
points = 0
attempts = 10
guessed_letters = []
correct_letters = []

# Display initial message
print("Welcome to Hangman!")
print(f"You have {attempts} total chances to get the word right")
print("_ " * word_len)

# Main game loop
while attempts > 0:
    # Get user's guess
    guess = input("Guess a letter: ").lower()

    # Validate the guess
    if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word_to_guess:
            correct_letters.append(guess)
            # Increase attempts and points based on word length and difficulty
            if difficulty != 5:
                attempts += 2
            points += ceil(word_len/2.6)
        else:
            # Decrease attempts if the guess is incorrect
            attempts -= 1
            print("\nIncorrect Guess")
            print(f'{attempts} remaining')

        # Display the current state of the word
        current_word = ""
        for letter in word_to_guess:
            if letter in correct_letters:
                current_word += letter + " "
            else:
                current_word += "_ "
        print(current_word)

        # Check if the word has been completely guessed
        if set(word_to_guess) == set(correct_letters):
            print("Congratulations! You've guessed the word: " + word_to_guess)
            break
    else:
        print("Invalid guess. Please enter a single letter you haven't guessed before.")

# End of game
if attempts == 0:
    print("You're out of attempts. The word was: " + word_to_guess)

# Display earned points
print("Points Earned: " + str(points))
