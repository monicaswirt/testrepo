import random

def guess(x):
    randomno=random.randint(1,x)
    guess=0
    while guess!= randomno:
        guess=int(input(f"Enter a number between one and {x}"))

        if guess <randomno:
            print("Sorry try again.The number is low")
            
        elif guess > randomno:
            print("Sorry try again.The number is high")
            
    print("Congratulatonss!You gueessed it right")


guess(10)