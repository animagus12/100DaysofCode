import datetime as dt
import smtplib
from random import choice


my_email = "neongen18@gmail.com"
password = "Sbp@2001"


with open("Python/#100DaysOfCode/Day 32/quotes.txt") as file:
    quotes = file.readlines()
    

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= "subhrajit_panda@yahoo.com", 
            msg= f"Subject:Monday Motivation\n\n{choice(quotes)}")

