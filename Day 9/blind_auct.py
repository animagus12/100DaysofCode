from art import logo
import os

auction_dict = []
def auction(name, bid):
    auction_dict.append({"name": name, "bid": bid})

rerun = True
while rerun:
    os.system('cls')
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction(name, bid)
    direction = input("Are ther any other bidders? Type 'yes' or 'no'.")
    if (direction == 'no'):
        os.system('cls')
        print(logo)
        rerun = False
        name_list = []
        bid_list = []
        for i, dict in enumerate(auction_dict):
            name_list.append(dict["name"])
            bid_list.append(dict["bid"])
        
        max_value = max(bid_list)
        max_index = bid_list.index(max_value)
        print(f"The winner is {name_list[max_index]} with a bid of ${max_value}.")