from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

URL_ZILLOW = os.getenv('URL_ZILLOW')


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.instagram.com/")

response = requests.get(URL_ZILLOW)
soup = BeautifulSoup(response.text, "html.parser")

