#This program will run a random rock paper scissors against the computer
#Showing your W or L streak
#Might add a two player mode

#import statement
import random
from getpass import getpass

#welcome message
print("\n")
print("--- Welcome to the Rock-Paper-Scissors game ---")
def menu():
    print("Select one of the following options (Type just the number) ")
    print("1. Rock ")
    print("2. Paper ")
    print("3. Scissors ")
    print("\n")

#constants
options_dictionary = {
    1: "ROCK",
    2: "PAPER",
    3: "SCISSORS"
}

# beats_dictionary = {
#    1: 3, #Rock beats Scissors
#    2: 1, #Paper beats Rock
#    3: 2  #Scissors beats Paper
#}

#variable that allows the user to play again
again = 1
wins = 0
losses = 0

#shoot message
def shoot_message():
    print("Rock Paper Scissors... Shoot! ")

while again == 1:
    menu()
    user_choice = int(input("Your choice: "))
    shoot_message()
    computer_choice = random.randint(1, 3)

    if user_choice == computer_choice:
        print(f"That's a draw! You both chose {options_dictionary[user_choice]}! ")
        print("\n")

    #when PAPER beats ROCK
    elif user_choice == 1 and computer_choice == 2:
        print("Better luck next time! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        losses = losses + 1
        
    elif user_choice == 2 and computer_choice == 1:
        print("You won! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        wins = wins + 1


    #when ROCK beats SCISSORS 
    elif user_choice == 3 and computer_choice == 1:
        print("Better luck next time! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        losses = losses + 1

    elif user_choice == 1 and computer_choice == 3:
        print("You won! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        wins = wins + 1


    #when SCISSORS beats PAPER
    elif user_choice == 2 and computer_choice == 3:
        print("Better luck next time! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        losses = losses + 1

    elif user_choice == 3 and computer_choice == 2:
        print("You won! ")
        print(f"You chose {options_dictionary[user_choice]} and the computer chose {options_dictionary[computer_choice]}\n")
        wins = wins + 1

    
    again = int(input("Press 1 to continue or 2 to quit "))


print(f"--- Your Ws: {wins} ---")
print(f"--- Your Ls: {losses} ---")
print("Thanks for playing. Come back soon! ")