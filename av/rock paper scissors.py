import random
import os
import shutil
import sys
from time import sleep

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def center_text(text):
    columns, _ = shutil.get_terminal_size((80, 20))
    return text.center(columns)

def get_odd_number():
    attempts = 0
    responses = [
        "Oops! That's even. Try again for a REAL challenge!",
        "Still even! Come on, I believe in you!",
        "Hint: It's... not even. One more shot?",
        "Alright, alright. Odd numbers only, please!"
    ]

    while True:
        try:
            num = int(input("\n\nHow many rounds do you want to play?[Choose an odd number]: "))

            if num % 2 == 0:
                print(center_text(responses[attempts % len(responses)]))
                attempts += 1
            else:
                return num
        except ValueError:
            print(center_text("That's not a number at all! Try again."))

options = ["ROCK", "PAPER", "SCISSORS"]
option_numbers = {"1": "ROCK", "2": "PAPER", "3": "SCISSORS"}

print("\n\n\n")
print(center_text("\u001b[36;1mROCK   PAPER   SCISSORS"))
sleep(2)
clear_terminal()

rounds = get_odd_number()
user_score = 0
computer_score = 0

for round in range(rounds):
    while True:
        user_choice = input("\n\n\u001b[36;1mChoose your move:\n[1] ROCK\n[2] PAPER\n[3] SCISSORS\n\n\n").strip()
    
        if user_choice in option_numbers:
            user = option_numbers[user_choice]
            break
        else:
            print(center_text("Oops! That's not a valid choice. Retry this round."))
            sleep(2)
            clear_terminal()

    computer = random.choice(options)
    sleep(1)
    clear_terminal()
    print("\n\n\n")
    print(center_text(f"\u001b[34mRound {round+1}/{rounds}"))
    print("\n")
    print(center_text(f"\u001b[34mYOU CHOSE: [{user}]  COMPUTER CHOSE: [{computer}]"))
    print("\n")

    if user == computer:
        print(center_text(f"\u001b[33;1mBOTH CHOSE {user}. IT'S A TIE!"))
    elif user == "ROCK":
        if computer == "SCISSORS":
            print(center_text("\u001b[32;1mROCK SMASHES SCISSORS! YOU WIN!"))
            user_score += 1
        else:
            print(center_text("\u001b[31;1mPAPER COVERS ROCK! YOU LOSE."))
            computer_score += 1
    elif user == "PAPER":
        if computer == "ROCK":
            print(center_text("\u001b[32;1mPAPER COVERS ROCK! YOU WIN!"))
            user_score += 1
        else:
            print(center_text("\u001b[31;1mSCISSORS CUTS PAPER! YOU LOSE."))
            computer_score += 1
    elif user == "SCISSORS":
        if computer == "PAPER":
            print(center_text("\u001b[32;1mSCISSORS CUTS PAPER! YOU WIN!"))
            user_score += 1
        else:
            print(center_text("\u001b[31;1mROCK SMASHES SCISSORS! YOU LOSE."))
            computer_score += 1
    else:
        print(center_text("Oops! Something went wrong. Retry this round."))
    sleep(2)
    clear_terminal()

print("\n\n\n")
print(center_text(f"\u001b[34mCOMPUTER SCORE: {computer_score}  USER SCORE: {user_score}"))

if user_score > computer_score:
    print(center_text("\u001b[32;1mYAAY! YOU WON THE GAME :D\n"))
elif user_score == computer_score:
    print(center_text("\u001b[33;1mITS A TIE :|\n"))
else:
    print(center_text("\u001b[31;1mYOU LOSE :(\n"))
