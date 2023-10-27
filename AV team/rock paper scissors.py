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

def centered_input(prompt):
    sys.stdout.write(center_text(prompt))
    sys.stdout.flush()
    return input()

def get_odd_number():
    attempts = 0
    playful_responses = [
        "Oops! That's even. Try again for a REAL challenge!",
        "Still even! Come on, I believe in you!",
        "Hint: It's... not even. One more shot?",
        "Alright, alright. Odd numbers only, please!"
    ]
    

    while True:
        try:
            
            num = int(input("\n\nHow many rounds do you want to play?[Choose an odd number]:"))

            if num % 2 == 0:
                print(center_text(playful_responses[attempts % len(playful_responses)]))
                attempts += 1
            else:
                return num
        except ValueError:
            print(center_text("That's not a number at all! Try again."))

options = ["ROCK", "PAPER", "SCISSORS"]
clear_terminal()
print("\n\n\n")
print(center_text("\u001b[36;1mROCK   PAPER   SCISSORS"))
sleep(2)
clear_terminal()

rounds = get_odd_number()
clear_terminal()
user_score = 0
computer_score = 0

for round in range(rounds):
    user = input("\n\n\u001b[36;1mROCK ? PAPER? SCISSORS? ").upper()
    computer = random.choice(options)

    print(center_text(f"\u001b[34mRound {round+1}/{rounds}"))
    print(center_text(f"\u001b[34mYOU CHOSE: [{user}]  COMPUTER CHOSE: [{computer}]"))

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
        print(center_text("\u001b[31;1mOops! Didn't catch that. Make sure it's either ROCK, PAPER, or SCISSORS!"))

    sleep(3)
    clear_terminal()
print("\n\n\n")
print(center_text(f"\u001b[34mCOMPUTER SCORE: {computer_score}  USER SCORE: {user_score}"))

if user_score > computer_score:
    print(center_text("\u001b[32;1mYAAY! YOU WON THE GAME :D"))
elif user_score == computer_score:
    print(center_text("\u001b[33;1mITS A TIE :|"))
else:
    print(center_text("\u001b[31;1mYOU LOSE :("))

