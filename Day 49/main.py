from selenium import webdriver
from creds import URL, EMAIL, PASSWORD, PHONE
import time

chrome_driver_path = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

signin = driver.find_element_by_link_text("Sign in")
signin.click()

username = driver.find_element_by_name("session_key")
username.send_keys(EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)

login = driver.find_element_by_css_selector(".login__form_action_container button")
login.click()

jobs = driver.find_elements_by_css_selector(".jobs-search-results__list-item")

for job in jobs:
    print("called")
    job.click()
    time.sleep(2)
    try:
        easy_apply = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
        easy_apply.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit = driver.find_element_by_css_selector("footer div button")
        submit.click()

        if submit.get_attribute("artdeco-button__text") != ("artdeco-button__text"):
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit.click()
    
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
        
    except:
        continue







# driver.close() # one tab
