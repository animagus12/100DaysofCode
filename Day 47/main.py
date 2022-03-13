import requests
from bs4 import BeautifulSoup
import smtplib
from creds import *

# Scrapping the specific link for current prices
response = requests.get(PRODUCT_URL, headers=header).text
soup = BeautifulSoup(response, "html.parser")
current_price = soup.find(
    name="span",
    class_="a-price-whole").get_text().rstrip(".")

# Title of the product
title = soup.find(
    name="span",
    class_="a-size-large product-title-word-break",
    id="productTitle").get_text(strip=True)

# Checking weather the prices has dropped and sending an alert
if int(current_price.replace(",", "")) <= FINAL_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SENDER_EMAIL,
            msg=f"Subject:Price Drop Alert\n\n{title} has dropped to ₹{FINAL_PRICE}\nLink: {PRODUCT_URL}")
