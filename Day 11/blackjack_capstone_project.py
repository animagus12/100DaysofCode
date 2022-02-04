from random import randint
from art import logo
import os

def black_jack():
    print(logo)

    # The Deck Of Cards 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Geneartes a Random Card from the Deck
    def rng():
        rn = randint(0, len(cards) - 1)
        return (cards[rn])

    # Function to make the dealer's hand
    def dealer():
        global d_list
        d_list = []
        d_list.append(rng())
        d_list.append(rng())
        if sum(d_list) <= 17:
            d_list.append(rng())
            

    # Function to make the player's hand 
    def player():
        global p_list
        p_list = []
        p_list.append(rng())
        p_list.append(rng())
        print(f"\tYour cards : {p_list}, current score: {sum(p_list)}")
        print(f"\tComputer's first card: {d_list[0]}")
        
    dealer()
    player()

    # Giving choice to the player to get another card
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    while choice == 'y':
        if sum(d_list) > 21:
            break
        p_list.append(rng())
        print(f"\tYour cards: {p_list}, final score: {sum(p_list)}")
        print(f"\tComputer's first card: {d_list[0]}")
        if sum(p_list) > 21:
            break
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
    print(f"\tYour final hand: {p_list}, final score: {sum(p_list)}")
    print(f"\tComputer's final hand: {d_list}, final score: {sum(d_list)}")
    if sum(p_list) > 21:
        print("You went over. You lose 😭")
    elif sum(d_list) > 21:
        print("Opponent went over. You win 😁")
    else:
        # Checking who won the round
        if sum(d_list) == 0:
            print("Lose, opponent has Blackjack 😱")
        elif sum(p_list)  == 0:
            print("Win with a Blackjack 😎")
        elif sum(p_list) > sum(d_list):
            print("You win 😃")
        elif sum(p_list) < sum(d_list):
            print("You lose 😤")
        else:
            print("Draw 🙃")

initial_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while initial_choice == 'y':
    os.system('cls')
    black_jack()
    initial_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

