from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Optional - Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open the LinkedIn jobs page
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%2BDeveloper&location=Sri%2BLanka&geoId=100446352&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4223533819&position=24&pageNum=0")

# Allow the page to load
time.sleep(3)

# Click the "Sign in" button
sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()


email = '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[1]/div[1]/div/div'
password = '//*[@id="base-sign-in-modal_session_password"]'
signing = '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button'


email_field = driver.find_element(By.XPATH, email)
email_field = driver.find_element(By.XPATH, email)