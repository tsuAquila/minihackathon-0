
data = ["goat", "dog", "gate"]

import random
stage = random.choice(data)

# Generate a random key for the rotation cipher
key = random.randint(-2, 2)
while key == 0:
    key = random.randint(-2, 2)


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

# Apply rotation cipher to the selected word
newstage = rotate(stage, key)

# Create a version of the word with underscores
underscored_stage = list(newstage)
if len(underscored_stage) > 6:
    for i in range(len(underscored_stage) // 3):
        num = random.randint(0, len(underscored_stage) - 1)
        underscored_stage[num] = "_"
newstage = "".join(underscored_stage)

print(newstage)

userv = input("Enter your Guess: ")
if userv == stage:
    print("Correct!")
else:
    print("Wrong! The word was:", stage)
