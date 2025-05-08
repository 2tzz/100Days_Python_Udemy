from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from dotenv import load_dotenv
import time


load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.linkedin.com/jobs/search?keywords=Python%2BDeveloper&location=Sri%2BLanka&geoId=100446352")

wait = WebDriverWait(driver, 10)


sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-in-modal__outlet-btn")))
sign_in_button.click()


email_field = wait.until(EC.presence_of_element_located((By.ID, "session_key")))
password_field = driver.find_element(By.ID, "session_password")
login_button = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')

email_field.send_keys(MY_EMAIL)
password_field.send_keys(MY_PASSWORD)
login_button.click()


time.sleep(5)


jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
jobs_available = [job.text for job in jobs]

print(f"Found {len(jobs_available)} jobs.")

posting_num = 0
while jobs_available:
    try:
        
        job_element = driver.find_element(By.LINK_TEXT, jobs_available[posting_num])
        job_element.click()
        time.sleep(2)

        
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-s-apply")
        apply_button.click()
        time.sleep(2)

      
        try:
            phone_input = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
            phone_input.clear()
            phone_input.send_keys(MY_PHONE_NUMBER)
            time.sleep(1)
        except NoSuchElementException:
            pass  

       
        try:
            driver.find_element(By.CSS_SELECTOR, 'footer button').click()  # Next or Review button
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Review your application"]').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Submit application"]').click()
            print(f" Applied to: {jobs_available[posting_num]}")
        except NoSuchElementException:
            print(f"⚠️ Couldn't complete application for: {jobs_available[posting_num]}")
        
    except (NoSuchElementException, ElementClickInterceptedException):
        print(f" Skipping job: {jobs_available[posting_num]}")


    jobs_available.pop(posting_num)
    time.sleep(2)

print(" All job applications attempted.")
