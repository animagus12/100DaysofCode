from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "C:/Users/subhr/OneDrive/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

# driver.close() # one tab
