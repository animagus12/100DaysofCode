# import smtplib

# my_email = "neongen18@gmail.com"
# password = "Sbp@2001"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password= password)
#     connection.sendmail(
#         from_addr= my_email, 
#         to_addrs= "subhrajit_panda@yahoo.com", 
#         msg= "Subject:Hello\n\nThis is the Body of my Email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year = 2001, month= 12, day= 12)
print(date_of_birth)