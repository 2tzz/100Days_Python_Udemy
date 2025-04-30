from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

events = {}

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value='fName')
l_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.TAG_NAME , value='button')







f_name.send_keys('thiyura')
l_name.send_keys('thilakshana')
email.send_keys('thilakhanathiyura@gmail.com')


button.click()

# <button class="btn btn-lg btn-primary btn-block" type="submit">Sign Up</button>