from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://x.com/i/flow/login")

login_entry = driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]')
login_entry.send_keys('thilakshana.100daysofcode@gmail.com')

