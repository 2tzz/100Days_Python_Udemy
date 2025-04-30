from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

events = {}

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_value = driver.find_element(By.XPATH , value='//*[@id="articlecount"]/ul/li[2]/a[1]')
articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

search_icon = driver.find_element(By.CSS_SELECTOR, value='#p-search a')

# article_link = driver.find_element(By.LINK_TEXT, value='initial campaign of the Breton Civil War')

search_bar = driver.find_element(By.NAME, value='search')

search_icon.click()
# article_link.click()

search_bar.send_keys('Python')

search_bar.send_keys(Keys.ENTER)