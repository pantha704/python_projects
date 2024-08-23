import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

UPLOAD = 49
DOWNLOAD = 49
TWITTER_EMAIL = "pantha704"
TWITTER_PASSWORD = "prathamj!"

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
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        # self.driver.implicitly_wait(15)
        # next = self.driver.find_element(By.XPATH,
        #                                 '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        # next.click()

        self.driver.implicitly_wait(15)
        password = self.driver.find_element(By.CSS_SELECTOR,
                                            '#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-1e084wi.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input')
        password.click()
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)


        self.driver.implicitly_wait(15)
        text = self.driver.find_element(By.CSS_SELECTOR,
                                        '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')

        # #react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div

        text.click()
        text.send_keys(
            f"@airtelindia @fiber_xstream\nHey mfs! I would like to kindly request you for improving your fkin internet speed of {speed[0]}mbps Download and {speed[1]}mbps Upload, which absolutely doesnt meet the fkin plan of mine, which you shit about at every end of the month for billings.\n")

        self.driver.implicitly_wait(15)
        tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet.click()

        print("Posted! :)")
        time.sleep(15)
    def sleep(self):
        time.sleep(111)

# chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chrome.exe"

driver = webdriver.Chrome()
# driver.get("https://github.com/pantha704")

bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()

if float(speed[0]) < DOWNLOAD or float(speed[1]) < UPLOAD:
    bot.tweet_at_provider()
bot.tweet_at_provider()
# bot.sleep()