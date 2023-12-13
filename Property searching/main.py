import time

import playsound
from bs4 import BeautifulSoup
from playsound import PlaysoundException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import requests

chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdAgUyTmUtHr9srg8N9_eOP4WGVO3U-twQSqRmkxWZ6-tdWJA/viewform?usp=sf_link'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q="
                       "0.9",
}

response = requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
                        "%22mapBounds%22%3A%7B%22west%22%3A-122.64409709342021%2C%22east%22%3A-122.10439372427959%2C"
                        "%22south%22%3A37.521418900376446%2C%22north%22%3A37.83227702080264%7D%2C%22mapZoom%22%3A11"
                        "%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D"
                        "%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A"
                        "%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C"
                        "%22isListVisible%22%3Atrue%7D", headers=HEADERS)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

address = soup.select(selector='.result-list-container a')
print(address)
# time.sleep(50)