from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv


load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\\Development\\chromedriver.exe")  

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%2BDeveloper&location=Sri%2BLanka&geoId=100446352&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=4223533819&position=24&pageNum=0")


wait = WebDriverWait(driver, 10)
sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-in-modal__outlet-btn")))
sign_in_button.click()


email_field = wait.until(EC.presence_of_element_located((By.ID, "session_key")))
password_field = wait.until(EC.presence_of_element_located((By.ID, "session_password")))
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')))


email_field.send_keys(MY_EMAIL)
password_field.send_keys(MY_PASSWORD)
login_button.click()

print("Sign-in completed.")
