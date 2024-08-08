import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER=""
PASSWORD=""
PROMISSED_UP = 80
PROMISSED_DOWN = 80

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver

    def get_internet_speed(self):

        self.driver.implicitly_wait(15)
        self.driver.get(url="https://www.speedtest.net/")

        self.driver.implicitly_wait(15)
        start_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '1]/a/span[4]')

        start_btn.click()

        down = None
        while down is None:
            # time.sleep(30)
            try:
                down = self.driver.find_element(By.CSS_SELECTOR,
                                                "#container > div > div.main-content > div > div > div > "
                                                "div.pure-u-custom-speedtest > "
                                                "div.speedtest-container.main-row > div.main-view > div > "
                                                "div.result-area.result-area-test > div > div > "
                                                "div.result-container-speed.result-container-speed-active > "
                                                "div.result-container-data > "
                                                "div.result-item-container.result-item-container-align-center > div > "
                                                "div.result-data.u-align-left > span").text
                up = self.driver.find_element(By.CSS_SELECTOR,
                                              "#container > div > div.main-content > div > div > div > "
                                              "div.pure-u-custom-speedtest > "
                                              "div.speedtest-container.main-row > div.main-view > div > "
                                              "div.result-area.result-area-test > div > div > "
                                              "div.result-container-speed.result-container-speed-active > "
                                              "div.result-container-data > "
                                              "div.result-item-container.result-item-container-align-left > "
                                              "div > div.result-data.u-align-left > span").text
            except:
                pass
            else:
                return [down, up]

    def tweet_at_provider(self):

        self.driver.implicitly_wait(15)
        self.driver.get(url="https://x.com/login")

        self.driver.implicitly_wait(15)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(USER)
        # print("try block")

        self.driver.implicitly_wait(15)
        next = self.driver.find_element(By.XPATH,
                                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next.click()

        self.driver.implicitly_wait(15)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.click()
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)


        self.driver.implicitly_wait(15)
        text = self.driver.find_element(By.CSS_SELECTOR,
                                        '#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')

        # #react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div

        text.click()
        text.send_keys(
            f"@airtelindia @fiber_xstream\nHey mfs! I would like to kindly request you for improving your fkin internet speed of {speed[0]}mbps Download and {speed[1]}mbps Upload, which absolutely doesnt meet the fkin plan of mine, which you shit about at every end of the month for billings.\n")

        self.driver.implicitly_wait(15)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                   '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                   '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div['
                                                   '3]/div/span/span')
        tweet.click()
        print("Posted! :)")
        time.sleep(15)



# chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chrome.exe"

driver = webdriver.Chrome()
# driver.get("https://github.com/pantha704")

bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()

if float(speed[0]) < PROMISSED_DOWN or float(speed[1]) < PROMISSED_UP:
    bot.tweet_at_provider()
bot.tweet_at_provider()

