from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv

load_dotenv()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class SpeedData():

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)