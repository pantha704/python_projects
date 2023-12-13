import threading
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)

cookie = driver.find_element(By.ID, 'bigCookie')

# # Making a list of ids of every item in the store
# itemss = driver.find_elements(By.CSS_SELECTOR, '#store .product.unlock.enabled')
# item_ids = [item.get_attribute("id") for item in itemss]
# # print(item_ids)
#
# timeout_inc = 5
# timeout = time.time() + timeout_inc  # 5 seconds
# five_min = time.time() + 60 * 5  # 5 minutes

while True:
    try:
        cookie.click()
    except:
        pass
    # if time.time() > timeout:
    #     # Re-find the items in the store before accessing their properties
    #     items = driver.find_elements(By.CSS_SELECTOR, "#store .product.enabled")
    #     prices = []
    #     for item in items:
    #         if item != '':
    #
    #             prices.append(item.text.split("\n")[1])
    #     print(prices)
    #     item_prices = []
    #     for price in prices:
    #         if "-" in price:
    #             price = int(price.split("-")[-1].replace(",", ""))
    #             item_prices.append(price)
    #
    #     # Noting all the ids and prices of items in the store
    #     cookie_upgrades = {}
    #     for n in range(len(item_prices)):
    #         cookie_upgrades[item_ids[n]] = item_prices[n]
    #
    #     # Getting the current cookie count
    #     cookies = driver.find_element(By.CSS_SELECTOR, "#cookies.title").text.split()[0]
    #     if "." in cookies:
    #         cookies = cookies.replace(".", "")
    #     cookies = int(cookies)
    #
    #     # Checking all the affordable items
    #     try:
    #         affordable = {}
    #         for id, cost in cookie_upgrades.items():
    #             if cost < cookies:
    #                 affordable[cost] = id
    #
    #         # Finding highest upgrade option
    #         # print(affordable)
    #         highest_upgrade = max(affordable.keys())
    #         item_to_upgrade = affordable[highest_upgrade]
    #         driver.find_element(By.ID, item_to_upgrade).click()
    #     except:
    #         continue
    #     else:
    #         timeout_inc += 5
    #         timeout = time.time() + timeout_inc
    #
    #         print(f"Item buying timeout increased to: {timeout_inc} seconds.\nTime now: {datetime.now().time()}")
    #     # After 5 minutes the bot will stop
    #     if time.time() > five_min:
    #         break
# print(driver.find_element(By.XPATH, '//*[@id="cookies"]').text)
# time.sleep(10)
# driver.quit()
