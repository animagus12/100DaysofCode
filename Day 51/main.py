from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from creds import URL, EMAIL, PASSWORD, PHONE
import time

URL = "https://www.speedtest.net"
PROMISED_DOWN = 150
PROMISED_IP = 10
CHROME_DRIVER_PATH = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service = driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(3)
        go = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_class_name(".upload-speed").text

        in_progress = True
        while in_progress:
            progress = self.driver.find_element_by_css_selector("overall-progress").text
            if progress.startswith("Your speed test has completed"):
                download_result = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
                upload_result = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')       
                print(f"Your download speed is {download_result.text} MBit/s and your upload speed is {upload_result.text} MBit/s")
                in_progress = False
            else:
                time.sleep(5)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(Service(CHROME_DRIVER_PATH))
bot.get_internet_speed()
bot.tweet_at_provider()


# login = self.driver.find_element_by_css_selector(".js-start-test .test-mode-multi")
# login.click()
