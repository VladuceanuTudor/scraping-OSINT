from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

import requests

def check_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    

def generate_usernames(first_name, last_name):
    usernames = [
        f"{first_name}{last_name}",
        f"{first_name}.{last_name}",
        f"{first_name}_{last_name}",
        f"{last_name}{first_name}",
        f"{last_name}.{first_name}",
        f"{last_name}_{first_name}",
        f"{first_name}{last_name[0]}",
        f"{last_name}{first_name[0]}",
        f"{first_name[0]}{last_name}",
        f"{last_name[0]}{first_name}"
    ]
    return usernames

def check_instagram_profile(username):
    service = Service(executable_path="./chromedriver")
    chrome_options = Options()
    #chrome_options.binary_location = "/usr/bin/google-chrome"  # Adjust this path if necessary
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)  # Allow time for page to load
        substring1 = "Sorry, this page isn't available."
        substring2 = "Something went wrong"
        
        if "Page Not Found" in driver.title:
            return False
        
        elements_with_text = driver.find_elements(By.XPATH, "//*[text()]")
        
        for element in elements_with_text:
            if substring2 == element.text:
                return True
        for element in elements_with_text:
            if substring1 == element.text:
                return False

        return True
    
    except Exception as e:
        print(f"Error checking Instagram profile: {str(e)}")
        return False
    
    finally:
        driver.quit()

# Update check_social_media_accounts function to use check_instagram_profile
def check_social_media_accounts(first_name, last_name):
    base_urls = {
        "Facebook": "https://www.facebook.com/",
        "Instagram": "https://www.instagram.com/",
        
    }

    usernames = generate_usernames(first_name, last_name)
    found_accounts = []

    for platform, base_url in base_urls.items():
        for username in usernames:
            url_to_check = base_url + username
            if platform == "Instagram":
                if check_instagram_profile(username):
                    found_accounts.append((platform, url_to_check))
            else:
                if check_url(url_to_check):
                    found_accounts.append((platform, url_to_check))
                    #time.sleep(1)  # Add a delay to avoid rate limiting

    if not found_accounts:
        print("No social media accounts found.")
    else:
        print("Found social media accounts:")
        for platform, url in found_accounts:
            print(f"{platform}: {url}")

# Example usage
print("-----------------------------------------------------------------")
first_name = input("Prenume: ").strip().lower()
last_name = input("Nume: ").strip().lower()
print("-----------------------------------------------------------------")

check_social_media_accounts(first_name, last_name)
print("-----------------------------------------------------------------")



print("-----------------------------------------------------------------")

# driver.quit()
