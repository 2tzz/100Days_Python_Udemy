
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


speed = '12'

# Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.speedtest.net/")

wait = WebDriverWait(driver, 30)

# Click "Go" button to start the test
start_button = wait.until(EC.element_to_be_clickable((By.XPATH , '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[2]/a/span[4]')))
start_button.click()

time.sleep(50)

# Wait until download result appears (typically takes ~40 seconds)
download_speed = driver.find_element(By.XPATH , '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

# Wait until upload result appears
upload_speed = driver.find_element(By.XPATH , '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

print(f"Download speed: {download_speed} Mbps")
print(f"Upload speed: {upload_speed} Mbps")



driver.get("https://x.com/i/flow/login")

wait = WebDriverWait(driver, 15)

# Step 1: Enter email
email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")))
email_input.send_keys("thilakshana.100daysofcode@gmail.com")

next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')))
next_button.click()

username_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
username_input.send_keys("speedcheck1234")

next_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')))
next_button2.click()
# Step 3: Enter password
password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
password_input.send_keys("alwisX@123")

# # Step 4: Final login
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')))
login_button.click()

post_text = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
post_text.send_keys(f"Hey @SLTmobitel my currunt 4g brodband download speed is {download_speed} Mbs.\n Upload speed is {upload_speed}. \n Is that the speed you can offer in 2025 ?")

post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')))
post_button.click()
