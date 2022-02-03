print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
n = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_total = (bill*tip)/100.0
total = (bill + tip_total)/n
print(f"Each person should pay: {total:1.1f}")
