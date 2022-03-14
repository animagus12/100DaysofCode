from selenium import webdriver

# URL = "http://orteil.dashnet.org/experiments/cookie/"
URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = "C:/Users/subhr/OneDrive/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

# game_is_on = True

cookie = driver.find_element_by_id("bigCookie")
# while game_is_on:
    # cookie.click()
for _ in range(16):
    cookie.click()

upgrades = driver.find_elements_by_class_name("product unlocked enabled")
for upgrade in upgrades:
    print(upgrade.text)

# driver.close()
