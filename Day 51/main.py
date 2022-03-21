from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from creds import PASS, PHONE, TWITTER
import time

URL = "https://www.speedtest.net"
CHROME_DRIVER_PATH = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get(URL)
        time.sleep(2)
        
        go = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()

        time.sleep(60)

        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get(TWITTER)
        time.sleep(2)
        email = self.driver.find_element_by_name("text")
        email.send_keys(PHONE)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        post = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(
            f"Hey Jio, my is internet speed {self.down} download/{self.up} upload is too good to be true!")

        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


bot = InternetSpeedTwitterBot(Service(CHROME_DRIVER_PATH))
bot.get_internet_speed()
bot.tweet_at_provider()
