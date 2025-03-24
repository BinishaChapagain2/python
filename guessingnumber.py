#guessing game 

import random
random.randint(1,100)
counter=1
jackpot=random.randint(1,100)
guess=int(input("Guess the number"))

while guess != jackpot:
    if guess < jackpot:
        print("guess heiger")
    else:
        print("guess lower")
    guess=int(input("again guess"))
    counter+=1

print("Right answer")
print("you took ",counter,"time guess right answr")

