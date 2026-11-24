## Welcome to Guess the number game
## Purpose: The system will choose a random number from 1 to 100.
## The user will then try to guess it! The user will receive some hints weather the secret number is greater than or smaller than the one chosen.
## Lets begin! 

## import random and getpass module
import random
## getpass works as input but doesn't show what's being typed
from getpass import getpass

##rules
print("Welcome to the Guess the Number Game! ")
print("Main menu: ")
print("1. Single player mode ")
print("2. Two player mode ")
option = int(input("Select an option: "))
print("")


if option == 1: 
    print("Single player mode: ")
    print("")
    print("Pick a number between 1 and 100 and try to guess the secret number with the least amount of attempts possible! ")
    print("Let's go! ")

    ## variables
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = 0
    #while loop
    while guess != secret_number:
        guess = int(input("Guess the number: "))

        #make the counter count!
        attempts = attempts + 1

        #if statementsss
        if guess > secret_number: 
            print("Too high! ")

        elif guess < secret_number:
            print("Too low! ")

        else:
            print(f"LFG! The secret number was {secret_number}! You guessed it on {attempts} attempts")


elif option == 2:
    
    ## variables
    attempts = 0
    guess = 0
    player_number = random.randint(1, 2)
    secret_number = int(getpass(f"Player {player_number} will pick a number between 1 and 100: "))
   
    if secret_number < 1 or secret_number > 100:
        raise ValueError("Guess must be between 1 and 100!")
   
    
    else:
 
        while guess != secret_number:
            guess = int(input("Guess the number: "))

            #make the counter count!
            attempts = attempts + 1

            #if statementsss
            if guess > secret_number: 
                print("Too high! ")

            elif guess < secret_number:
                print("Too low! ")

            else:
                print(f"LFG! The secret number was {secret_number}! You guessed it on {attempts} attempts")

else: 
    print("We're currently working on some updates⚒️. Please select option 1 or 2.")
