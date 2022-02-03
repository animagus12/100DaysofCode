# 🚨 Don't change the code below 👇
from math import e
from re import L


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1 = name1.lower()
n2 = name2.lower()

t1 = n1.count("t")
r1 = n1.count("r")
u1 = n1.count("u")
e1 = n1.count("e")
t2 = n2.count("t")
r2 = n2.count("r")
u2 = n2.count("u")
e2 = n2.count("e")
true_total = t1+t2+r1+r2+u1+u2+e1+e2

l1 = n1.count("l")
o1 = n1.count("o")
v1 = n1.count("v")
e1 = n1.count("e")
l2 = n2.count("l")
o2 = n2.count("o")
v2 = n2.count("v")
e2 = n2.count("e")
love_total = l1+l2+o1+o2+v1+v2+e1+e2

total = str(true_total) + str(love_total)


if int(total) < 10 or int(total) > 90:
    print("Your score is " + total + ", you go together like coke and mentos.")
elif int(total) > 40 and int(total) < 50:
    print("Your score is " + total + ", you are alright together.")
else: 
    print("Your score is " + total + ".")