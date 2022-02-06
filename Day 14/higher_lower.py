import art
from game_data import data
from random import randint
import os

# Function to compare and update the initial and score 
def compare():
    global score
    global initial
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if initial['follower_count'] > data[second_rn]['follower_count'] and choice == 'A':
        score += 1
        print(f"You're right! Current score: {score - 1}")

    elif data[second_rn]['follower_count'] > initial['follower_count'] and choice == 'B':
        initial = second
        score += 1
        print(f"You're right! Current score: {score - 1}")

    elif initial['follower_count'] == data[second_rn]['follower_count']:
        initial = second
        if choice == 'A' or choice == 'B':
            score += 1
            print(f"You're right! Current score: {score - 1}")

    else:
        os.system('cls')
        print(art.logo) 
        print(f"Sorry, that's wrong. Final score: {score - 1}")
        score = 0

# Initializing score
score = 1
# Genrating the very first entry
initial_rn = randint(0, len(data)-1)
initial = data[initial_rn]

while score != 0:   
    os.system('cls')
    print(art.logo) 
    # Printing updated initial entry
    print (f"Comapre A: {initial['name']}, a {initial['description']}, from {initial['country']}")
    print(art.vs)
    # Genrating and printing second entry
    second_rn = randint(0, len(data)-1)
    second = data[second_rn]
    print (f"Comapre B: {data[second_rn]['name']}, a {data[second_rn]['description']}, from {data[second_rn]['country']}")
    
    compare()
