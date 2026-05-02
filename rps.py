import random

x = input("Do you want to play rock,paper,scissors?(y/n) : ").lower()
while True:
    if x == "y":
        user = input("select rock/paper/scissors(r/p/s) , select a to abort: ").lower()
        comp = random.choice(["rock","paper","scissors"])

        if comp == 'rock' and user == 'p':
            print("computer chose rock,you won!!")
        elif comp == 'rock' and user == 's' :
            print("computer chose rock, you lose")
        elif comp == 'scissors' and user == 'p' :
            print("computer chose scissors, you lose")
        elif comp == 'scissors' and user == 'r' :
            print("computer chose scissors, you won")
        elif comp == 'paper' and user == 's' :
            print("computer chose paper, you won")
        elif comp == 'paper' and user == 'r' :
            print("computer chose paper, you lose")
        elif user == "a":
            print("thank you")
            break
        else:
            print("you both chose same ,try again")

    elif x == "n":
        print("thank you!!,better luck next time")

    else:
        print("invalid input")

    