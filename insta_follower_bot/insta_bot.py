import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


class InstaFollower():
    def __init__(self):
        self.driver = driver
        self.counter = 0

    def login(self, username, passwd):

        self.driver.get(url="https://www.instagram.com/")

        time.sleep(2)
        try:
            usr = (
                self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input"))
            usr.send_keys(username)
        except:
            pass

        # usr = get_element(method="CSS_SELECTOR", path="#loginForm > div > div:nth-child(1) > div > label > input")
        # usr.send_keys(USERNAME)

        password = (
            self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input"))
        password.send_keys(passwd)
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        # saving info
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div['
                                               '2]/section/main/div/div/div/section/div/button').click()
        except:
            pass

        time.sleep(2)
        # turning on notifications
        try:
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div['
                                     '2]/div/div/div[3]/button[1]').send_keys(Keys.ENTER)
        except:
            pass

        # time.sleep(50)

    def find_and_follow(self, name):
        self.driver.get(url=f"https://www.instagram.com/{name}")
        time.sleep(5)
        try:
            followers = self.driver.find_element(By.CSS_SELECTOR, '._alvs ._ac2a')
            followers.click()
            # followers.send_keys(Keys.ENTER)
            print("success")
        except:
            print("f")
            pass

        # time.sleep(50)

    def following(self):
        time.sleep(5)
        peeps = self.driver.find_elements(By.CSS_SELECTOR, "._aano ._acap")
        for ppl in peeps:
            try:
                peeps[self.counter].click()
            except IndexError:
                if len(peeps) <= self.counter+1:
                    return
                else:
                    self.counter -= 1
            except:
                try:
                    dont_un_flw = self.driver.find_element(By.CLASS_NAME, "_a9_1")
                    dont_un_flw.click()
                except:
                    pass
            # time.sleep(1)
            self.counter += 1
            print("followed", self.counter, len(peeps))

        time.sleep(5)
        print("Scroll complete!")
        self.following()
