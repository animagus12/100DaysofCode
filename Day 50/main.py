from selenium import webdriver
# from creds import URL, EMAIL, PASSWORD, PHONE
# import time

URL = "https://tinder.com/"

chrome_driver_path = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

login = driver.find_element_by_link_text("Log in")
login.click()

google = driver.find_element_by_link_text("Log in with Google")
google.click()

