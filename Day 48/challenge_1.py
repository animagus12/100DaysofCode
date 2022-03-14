from selenium import webdriver

URL = "https://www.python.org"

chrome_driver_path = "C:/Users/subhr/OneDrive/Documents/Programs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

event_dates = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu li time")
event_names = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu li a")

events = {}
for n in range(len(event_dates)):
    events[n] = {
        "date" : event_dates[n].text,
        "event" : event_names[n].text,
    }
print(events)
driver.close() # one tab
