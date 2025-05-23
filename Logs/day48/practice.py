from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.python.org")


# price_dollar = driver.find_element(By.CLASS_NAME , value="a-price-whole" )
# price_cents = driver.find_element(By.CLASS_NAME , value="a-price-fraction"  )
# print(f"The price is {price_dollar.text}.{price_cents.text}")


button = driver.find_element(By.ID , value="submit")
print(button.size)


documentation_link = driver.find_element(By.CSS_SELECTOR , value=".documentation-widget a")
print(documentation_link.text)

bug_link= driver.find_element(By.XPATH , value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


driver.quit()