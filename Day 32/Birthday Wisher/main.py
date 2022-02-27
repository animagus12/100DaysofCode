import pandas
import smtplib
import datetime as dt
from random import choice

my_email = "subhrajit_panda@yahoo.com"
password = "grcnzyctugmzlpwk"

# Update the birthdays.csv
list_file = pandas.read_csv(
    "birthdays.csv")
all_data = list_file.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
letter_names = ["letter_1", "letter_2", "letter_3"]

for entry in all_data:
    if (now.month == entry['month'] and now.day == entry['day']):

        # If true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/{choice(letter_names)}.txt") as template:
            mail_text = template.read()
        final_mail = mail_text.replace("[NAME]", entry['name'])

# Send the letter to that person's email address.
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=entry['email'],
                msg=f"Subject:Happy Birthday\n\n{final_mail}")
