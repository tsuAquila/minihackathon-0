import random
import os
from time import sleep


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

options = [" ROCK", "PAPER", "SCISSORS"]
print("\n\n\n\t\t\t\tROCK   PAPER   SCISSORS")
sleep(3)
clear_terminal()

rounds = int(input("\n\t\t\t\t\u001b[34m ENTER THE NUMBER OF ROUNDS YOU WANNA PLAY: "))
clear_terminal()
user_score = 0
computer_score = 0

for round in range(rounds):
    user = input(f"\n\n\t\t\t\t\u001b[36;1m ROCK ? PAPER? SCISSORS? : ").upper()
    computer = random.choice(options)

    print(f"\n\n\t\t\t\t\tRound {round+1}/{rounds}")
    print(f"\n\n\t\t\t\t\u001b[34m  YOU CHOSE: [{user}] COMPUTER CHOSE: [{computer}]")

    if user == computer:
        print(f"\n\t\t\t\t \u001b[33;1m BOTH CHOSE {user}. IT'S A TIE!")
    elif user == "ROCK":
        if computer == "SCISSORS":
            print("\n\t\t\t\t \u001b[32;1mROCK SMASHES SCISSORS! YOU WIN!")
            user_score += 1
        else:
            print("\n\t\t\t\t \u001b[31;1mPAPER COVERS ROCK! YOU LOSE.")
            computer_score += 1
    elif user == "PAPER":
        if computer == "ROCK":
            print("\n\t\t\t\t \u001b[32;1mPAPER COVERS ROCK! YOU WIN!")
            user_score += 1
        else:
            print("\n\t\t\t\t \u001b[31;1mSCISSORS CUTS PAPER! YOU LOSE.")
            computer_score += 1
    elif user == "SCISSORS":
        if computer == "PAPER":
            print("\n\t\t\t\t \u001b[32;1mSCISSORS CUTS PAPER! YOU WIN!")
            user_score += 1
        else:
            print("\n\t\t\t\t \u001b[31;1mROCK SMASHES SCISSORS! YOU LOSE.")
            computer_score += 1
    else:
        print("\n\t\t\t\tCHECK SPELLINGGGG")

    sleep(4)
    clear_terminal()

print(f"\n\t\t\t\t COMPUTER SCORE:{computer_score} \t USER SCORE: {user_score}")

if user_score > computer_score:
    print("\n\t\t\t\t YAAY YOU WON THE GAME :D")
elif user_score == computer_score:
    print("\n\t\t\t\t\t\t\u001b[33;1m ITS A TIE :|")
else:
    print("\n\t\t\t\t\t\t\u001b[34;1m YOU LOSE :(")
