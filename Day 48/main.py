from selenium import webdriver

PRODUCT_URL = "https://www.amazon.in/OnePlus-10000-Charging-Lithium-Polymer/dp/B08HRZ3MXK/ref=nav_ya_signin?crid=18LIIYXWPILJM&keywords=power%2Bbank%2Boneplus&qid=1647176698&sprefix=power%2Bbank%2Bonel%2Caps%2C369&sr=8-1&th=1"

chrome_driver_path = "C:/Users/subhr/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(PRODUCT_URL)

# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

# price = driver.find_element_by_xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')
# print(price.text)

# driver.close() # one tab
driver.quit() # entire browser


