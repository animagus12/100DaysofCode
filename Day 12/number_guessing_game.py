from art import logo
from random import randint
import sys

# Random Number Generator in range 1 to 100
global rng
rng = str(randint(1, 100))

# Function to check the users guess
def guesser(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if guess > rng:
            attempts -= 1
            print("Too high")
            print("Guess again.")
        elif guess < rng:
            attempts -= 1
            print("Too Low")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {rng}")
            # Forceful Termination if the user wins
            sys.exit()
    print("You've run out guesses, you lose.")

print (logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Setting difficulty to the game
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    guesser(10)
elif difficulty == 'hard':
    guesser(5)
else:
    print("Please enter a valid choice!")












