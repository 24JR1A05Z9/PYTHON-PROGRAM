import random;
a=random.randrange(1,10);
guess=0
while guess!=a:
    guess=int(input("guess a number between 1 and 10:"))
    if guess==a:
        print("well guesses!")
