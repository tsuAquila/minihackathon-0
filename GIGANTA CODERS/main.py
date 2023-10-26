from data import data
score=0
life =5
import random

print("""
Hey there!!!
      Welcome to our word guess game

      Here are the instructions:
      1. The letters in the words will be shifted by a range of -3 to 3, just like in Caesar Cipher
      2. Some of the letters will be missing too.
      3. You have 5 lifes.
      4. You got 2 chances to guess the word.
      5. Don't worry, 4 options will also be provided.
      6. If not able to guess the word in 2 chances 1 life will be lost.

      What to wait, let's play!!!

""")
def rotate(text, key):
    ref_a = "abcdefghijklmnopqrstuvwxyz"
    ref_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_a = ref_a[key:] + ref_a[:key]
    cipher_A = ref_A[key:] + ref_A[:key]
    final = ""
    for letter in text:
        if letter in ref_a:
            ind = ref_a.index(letter)
            final += cipher_a[ind]
        elif letter in ref_A:
            ind = ref_A.index(letter)
            final += cipher_A[ind]
        else:
            final += letter
    return final
while life >0:
    # Apply rotation cipher to the selected word
    stage = random.choice(data)

    # Generate a random key for the rotation cipher
    key = random.randint(-2, 2)
    while key == 0:
        key = random.randint(-2, 2)

    newstage = rotate(stage, key)

    #printing the options
    samelen =[]
    for i in data:
        if len(i) ==len(stage) and len(samelen)<3:
            samelen.append(i)
    if stage not in samelen:
        samelen.append(stage)
    random.shuffle(samelen)
    while len(samelen) <4:
        word=random.choice(data)
        if word not in samelen:
            samelen.append(word)
    print("Here are your choices:", ", ".join(samelen))
    print("")

    # Create a version of the word with underscores
    underscored_stage = list(newstage)
    if len(underscored_stage) > 6:
        for i in range(len(underscored_stage) //4 ):
            num = random.randint(0, len(underscored_stage) - 1)
            underscored_stage[num] = "_"
    newstage = "".join(underscored_stage)


    print("Find the word for:",newstage)
    chance =2
    while chance>0:

        userv = input("Enter your Guess: ")
        chance-=1
        if userv == stage:
            print("Correct!")
            score +=1
            print(f"Current score {score}.\n\n")
            break
        elif chance ==1:
            print("you have 1 more chance.")
        else:
            life -=1
            print("Wrong! The word was: ", stage,"\nSorry you lost 1 life.Lifes left : {life}","\n\n")
            
print(f"Congrats,You Scored {score}.")

