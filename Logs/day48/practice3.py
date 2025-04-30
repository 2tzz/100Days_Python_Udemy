from selenium import webdriver
from selenium.webdriver.common.by import By

events = {}

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_value = driver.find_element(By.XPATH , value='//*[@id="articlecount"]/ul/li[2]/a[1]')
articles = driver.find_element(By.ID, value='articlecount')

print(articles.text)