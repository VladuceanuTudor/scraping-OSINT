from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

import requests

def check_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.head(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
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

def check_social_media_accounts(first_name, last_name):
    base_urls = {
        "Facebook": "https://www.facebook.com/",
        "Instagram": "https://www.instagram.com/",
        "LinkedIn": "https://www.linkedin.com/in/",
        # Add more social media URLs here if needed
    }

    usernames = generate_usernames(first_name, last_name)
    found_accounts = []

    for platform, base_url in base_urls.items():
        for username in usernames:
            url_to_check = base_url + username
            if check_url(url_to_check):
                found_accounts.append((platform, url_to_check))
                #print(f"Found {platform} account: {url_to_check}")
            # Add a small delay to avoid rate limiting
            time.sleep(1)

    if not found_accounts:
        print("No social media accounts found.")
    else:
        print("Found social media accounts:")
        for platform, url in found_accounts:
            print(f"{platform}: {url}")

# Example usage
first_name = input("Prenume: ").strip().lower()
last_name = input("Nume: ").strip().lower()

check_social_media_accounts(first_name, last_name)

# driver.quit()