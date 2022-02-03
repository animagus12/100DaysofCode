import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose.") 
    sys.exit()

figures = [rock, paper, scissors]
print(figures[user_choice])

comp_choice = random.randint(0, 2)
print("Computer chose:")
print(figures[comp_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose.") 
if user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose")
elif comp_choice > user_choice:
    print("You lose")
elif comp_choice < user_choice:
    print("You win!")
elif user_choice == comp_choice:
    print("Draw")

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose.") 
# else:

#     figures = [rock, paper, scissors]
#     print(figures[user_choice])

#     comp_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(figures[comp_choice])

#     # if user_choice >= 3 or user_choice < 0:
#     #     print("You typed an invalid number, you lose.") 
#     if user_choice == 0 and comp_choice == 2:
#         print("You win!")
#     elif comp_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif comp_choice > user_choice:
#         print("You lose")
#     elif comp_choice < user_choice:
#         print("You win!")
#     elif user_choice == comp_choice:
#         print("Draw")


