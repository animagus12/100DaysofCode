# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
rem_age = 90-int(age)

days = rem_age*365
weeks = rem_age*52
mnths = rem_age*12

print(f"You have {days} days, {weeks} weeks, and {mnths} months left.")
