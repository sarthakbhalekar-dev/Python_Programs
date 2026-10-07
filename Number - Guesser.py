
from random import randint

print("Let's Play Guess The Number, I Will Choose Any Number From 1 - 10 , You Have To Guess It!")
count=0
while count<2:
    c=randint(1,10)
    user=int(input("Enter The Number: "))
    if c>user:
        print("Try Again! Your Number Is Smaller Than The Chosen Number!")
    elif c<user:
        print("Try Again! Your Number Is Greater Than The Chosen Number!")
    elif c==user:
        print("Correct! You Have Guessed The Number!")
        break
    count+=1
print("The Chosen Number Was: ",c)
