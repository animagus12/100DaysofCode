from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from creds import USERNAME, PASSWORD

URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"
ACCOUNT = "gaming"

class InstaFollowBot:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(f"{URL}accounts/login/")
    
        time.sleep(2)

        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)

        time.sleep(2)

        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(2)

        search = self.driver.find_element_by_css_selector("input")
        search.send_keys(ACCOUNT)

        time.sleep(2)

        self.driver.get(f"{URL}{ACCOUNT}/")

        time.sleep(2)

        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)

        modal = self.driver.find_element_by_xpath("//div[@Class='isgrP']")
        
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.is_selected()
                cancel_button.click()


bot = InstaFollowBot(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()