from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

import requests

def check_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            #print(f"URL '{url}' exists and is reachable.")
            return True
        else:
            #print(f"URL '{url}' returned status code: {response.status_code}")
            return False
    except requests.ConnectionError:
        print(f"Could not connect to URL '{url}'")
        return False


url_to_check = "http://facemuc.bom/wwssa[w321"
if check_url(url_to_check):
    print("yes")
    pass
else:
    print("no")
    pass


# driver.quit()