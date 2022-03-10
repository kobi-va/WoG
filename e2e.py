from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import os


os.chmod('./chromedriver', 0755) 
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-using")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)


def test_scores_service():
    browser.get("http://localhost:1234/")
    element = browser.find_element(By.XPATH, "/html/body/center/table/tbody/tr[2]/td")
    score = element.text
    if 1000 >= int(score) >= 1:
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        print("Sucess")
        sys.exit(0)
    else:
        print("Failure")
        sys.exit(-1)
    


main_function()
