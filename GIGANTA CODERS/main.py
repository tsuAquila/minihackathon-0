
import random

stage = random.choice(data)
key = random.randint(-4,4)
while key == 0:
    key = random.randint(-4,4)

#Cipher generation
def rotate(text, key):
    ref_a = "abcdefghijklmnopqrstuvwxyz"
    ref_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_a = ref_a[key:]+ref_a[:key]
    cipher_A = ref_A[key:]+ref_A[:key]
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

newstage=rotate(stage,key)
print(newstage)
userv=input("Enter your Guess:")
if userv ==stage:
    print("poli")
else:
    print("poda")
