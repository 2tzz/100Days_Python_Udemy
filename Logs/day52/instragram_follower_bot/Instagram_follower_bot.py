from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")

# Get cookie to click on.
email_field = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input")
email_field.send_keys ('thilakshana.100daysofcode@gmail.com')
password_field = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input" )
password_field.send_keys ('alwisPYTHON@123')

time.sleep(2)

login_btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button" )
login_btn.click()

time.sleep(10)

value = 1
is_on = True

while is_on :
    driver.get("https://www.instagram.com/explore/people/")
    while value < 30 :
        time.sleep(5)
        follow_button  = driver.find_element(By.XPATH , f"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[2]/div/div/div[{value}]/div/div/div/div[3]/div/button")
        time.sleep(2)
        follow_button.click()
        time.sleep(3)
        value += 1


