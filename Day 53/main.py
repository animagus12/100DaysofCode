from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from creds import URL, FORM, header

CHROME_DRIVER_PATH = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"

response = requests.get(URL, headers=header).text

soup = BeautifulSoup(response, "html.parser")

# Adding all links in a list
links = soup.find_all(name="a", class_="list-card-link")
links_list = [link.get("href") for link in links]
# print(links_list)

# Adding all the prices in a list
prices = soup.find_all(name="div", class_="list-card-price")
price_list = []
for i in prices:
    price = i.text
    new_price = price
    for character in price:
        if not character.isdigit():
            new_price = new_price.replace(character, "")
    price_list.append(new_price)
# print(price_list)

# Adding all addresses in a list
addresses = soup.find_all(name="address", class_="list-card-addr")
address_list = [address.text for address in addresses]
# print(address_list)

# Making a webdriver
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(FORM)

time.sleep(2)

for i in range(len(address_list)):
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])

    time.sleep(2)

    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])

    time.sleep(2)

    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links_list[i])

    time.sleep(2)

    submit_button = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(2)

    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

    time.sleep(2)
