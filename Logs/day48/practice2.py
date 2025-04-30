from selenium import webdriver
from selenium.webdriver.common.by import By

events = {}

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.python.org/events")


event_elements = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events.menu li")


for i, event in enumerate(event_elements):
    time = event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    title = event.find_element(By.TAG_NAME, "a").text
    events[i] = {'time': time, 'event': title}


print(events)