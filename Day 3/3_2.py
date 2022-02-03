# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = weight / (height**2)
bmi = round(x)

if bmi < 18.5:
    state = "are underweight"
elif bmi > 18.5 and bmi < 25:
    state = "have a normal weight"
elif bmi > 25 and bmi < 30:
    state = "are slightly overweight"
elif bmi > 30 and bmi < 35:
    state = "are obese"
elif bmi > 35: 
    state = "are clinically obese"

print ("Your BMI is " + str(bmi) + ", you " + state)