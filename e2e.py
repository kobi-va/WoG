from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys

chrome_options = Options()
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/95.0.4638.69 Safari/537.36")
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)


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
