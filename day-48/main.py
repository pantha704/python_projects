
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless")

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
time.sleep(2)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
cursor = driver.find_element(By.XPATH, "//*[@id='buyCursor']/b")
grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
my_cookies = driver.find_element(By.XPATH, '//*[@id="money"]').text

# Making a list of ids of every item in the store
itemss = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in itemss]

timeout_inc = 5
timeout = time.time() + timeout_inc  # 5 seconds
five_min = time.time() + 60 * 5  # 5 minutes

while True:

    cookie.click()

    if time.time() > timeout:
        # Re-find the items in the store before accessing their properties
        items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        for item in items:
            try:
                prices.append(item.text)
            except:
                continue
        item_prices = []
        for price in prices:
            if "-" in price:
                price = int(price.split("-")[-1].replace(",", ""))
                item_prices.append(price)

        # Noting all the ids and prices of items in the store
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_ids[n]] = item_prices[n]

        # Getting the current cookie count
        cookies = driver.find_element(By.ID, "money").text
        if "," in cookies:
            cookies = (cookies.replace(",", ""))
        cookies = int(cookies)

        # Checking all the affordable items
        try:
            affordable = {}
            for id, cost in cookie_upgrades.items():
                if cost < cookies:
                    affordable[cost] = id

            # Finding highest upgrade option
            print(affordable)
            highest_upgrade = max(affordable.keys())
            item_to_upgrade = affordable[highest_upgrade]
            driver.find_element(By.ID, item_to_upgrade).click()
        except:
            continue
        else:
            timeout_inc += 5
            timeout = time.time() + timeout_inc

            print(f"Item buying timeout increased to: {timeout_inc} seconds.\nTime now: {datetime.now().time()}")
        # After 5 minutes the bot will stop
        if time.time() > five_min:
            break
print(driver.find_element(By.ID, "money").text)
time.sleep(10)
driver.quit()

# driver.get(url="http://secure-retreat-92358.herokuapp.com/")
#
# fName = driver.find_element(By.NAME, "fName")
# # fName.click()
# fName.send_keys("Pratham")
#
# lName = driver.find_element(By.NAME, "lName")
# # lName.click()
# lName.send_keys("Jaiswal")
#
# email = driver.find_element(By.NAME, "email")
# email.send_keys("prathamjaiswal204@gmail.com")
#
# btn = driver.find_element(By.TAG_NAME, "button")
# btn.click()
#
# time.sleep(5)
#
# driver.quit()
