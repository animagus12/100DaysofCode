from selenium import webdriver

URL = "http://secure-retreat-92358.herokuapp.com"

chrome_driver_path = "C:/Users/subhr/OneDrive/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Subhrajit")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Panda")
email = driver.find_element_by_name("email")
email.send_keys("subhra.jit748@gmail.com")
btn = driver.find_element_by_css_selector(".form-signin button")
btn.click()
