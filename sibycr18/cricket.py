from random import randint
from random import choice
import inflect
p = inflect.engine()
from time import sleep

# Read and display scores from the text file
with open("cricket_scores.txt", "r") as file:
    high_scores = file.readlines()

print("\n**Scoreboard**")
for score in high_scores:
    print(score.strip())  # Print each score, stripping newline characters

# If you want to display the top N scores, you can modify the loop like this:
# for index, score in enumerate(scores[:N], start=1):
#     print(f"{index}. {score.strip()}")

# Format of dict -> {question number : [question(with options), correct_choice]}
trivia_questions = {
    1 : ["Which of these cricket tournaments is played between international teams? \n(a) IPL\n(b) PSL\n(c) T20 World Cup\n(d) Big Bash League", "c"],
    2 : ["How many players are in a cricket team? \n(a) 9\n(b) 10\n(c) 11\n(d) 12", "c"],
    3 : ["Where is the sports stadium, ‘Green Park’ located? \n(a) Kanpur\n(b) Jamshedpur\n(c) Cutlack\n(d) Patiala", "a"],
    4 : ["The international governing body of cricket is? \n(a) CCI\n(b) GCI\n(c) LIC\n(d) ICC", "d"],
    5 : ["Which of these teams has won the most ICC Champions Trophy titles? \n(a) India\n(b) Australia\n(c) South Africa\n(d) Sri Lanka", "b"]
}
trivia_score = 0

your_name = input("\nEnter your name: ")

print("\n\t--- Answer 5 cricket trivia questions. Your trivia score will decide the player you get to bat... Good luck! ---\n")
print("\t\t\t*** Note that players with more ratings score more runs and have more wickets ***\n")


available_questions = list(trivia_questions.keys())
for i in range(5):
    question_number = choice(available_questions)
    print('Q) ' + trivia_questions[question_number][0])
    annswer = input("\nEnter your choice: ").strip().strip(')').strip('(').lower()
    if annswer == trivia_questions[question_number][1]:
        print("\nCorrect Answer...")
        trivia_score += 1
        print("Current Score: ", trivia_score)
    else:
        print("\nIncorrect Answer...")
    print()
    available_questions.remove(question_number)
print("\nYou Scored", trivia_score)

players = {
    9 : ["Virat Kohli", "Rohit Sharma", "Ravindra Jadeja"],
    7 : ["Shreyas Iyer", "KL Rahul", "Shubhman Gill"],
    5 : ["Shikhar Dhawan", "Ishan Kishan", "Washington Sundar"]
}
if trivia_score <= 2:
    your_player_rating = 5
    wickets_left = 0
elif trivia_score <= 4:
    your_player_rating = 7
    wickets_left = 1
else:
    your_player_rating = 9
    wickets_left = 2

your_player = choice(players[your_player_rating])
print("\nYour player is " + your_player)
print("Rating:", your_player_rating)

print("\n\tLETS BEGIN THE MATCH!\n")

runs_scored = 0

# Define bowlers with different types: fast, medium, and slow
bowlers = {
    "fast": {"chance_of_out": 3, "runs_conceded": [0, 1, 2, 4, 6]},
    "spin": {"chance_of_out": 2, "runs_conceded": [0, 1, 2, 3, 4]},
    "slow": {"chance_of_out": 1, "runs_conceded": [0, 1, 1, 2, 3]}
}

# Determine the type of bowler based on random choice
bowler_type = choice(["fast", "spin", "slow"])

print(f"You got a {bowler_type.capitalize()} bowler...")

# Simulate one over of the match
for i in range(6):  # 1 over contains 6 balls
    # Simulate the bowler's delivery
    is_out = randint(1, 10) <= bowlers[bowler_type]["chance_of_out"]
    # print(f'{is_out = }')
    
    if not is_out:  # Player is not out, continue playing
        runs_this_ball = choice(bowlers[bowler_type]["runs_conceded"])
        print(f"You scored {runs_this_ball} runs on {p.ordinal(i+1)} ball!")
        runs_scored += runs_this_ball
    else:  # Player is out
        print(f"\nOh no! You're out on {p.ordinal(i+1)} ball!\n")
        # print("--Answer this question to get more life--")
        if wickets_left != 0:
            print(f"You got {wickets_left} more wickets left...")
            continue
        else:
            print(f"No more wickets left...")
            break

    sleep(0.5)

print("\nIn your 1 over, you scored", runs_scored, "runs.")

# Higher-rated players have a better chance of not getting out and scoring more runs
if your_player_rating == 9:
    runs_scored *= 2  # Double the runs scored by the highest-rated player
    print("\nTotal runs scored(x2 for 9 rated player):", runs_scored)
elif your_player_rating == 7:
    runs_scored += 2  # Add 2 runs for the medium-rated player
    print("\nTotal runs scored (+2 for 7 rated player):", runs_scored)


# Store scores in a text file
with open("cricket_scores.txt", "a") as file:
    file.write(f"{your_name}  {runs_scored}\n")