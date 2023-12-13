import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.up = PROMISSED_UP
        self.down = PROMISSED_DOWN

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        start_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        try:
            start_btn.click()
        except:
            time.sleep(10)
            start_btn.click()

        down = None
        while down == None:
            # time.sleep(30)
            try:
                down = self.driver.find_element(By.CSS_SELECTOR,
                                                "#container > div > div.main-content > div > div > div > "
                                                "div.pure-u-custom-speedtest > "
                                                "div.speedtest-container.main-row > div.main-view > div > "
                                                "div.result-area.result-area-test > div > div > "
                                                "div.result-container-speed.result-container-speed-active > "
                                                "div.result-container-data > "
                                                "div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span").text
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
                return down, up

    def tweet_at_provider(self):
        self.driver.get(url="https://x.com")
        time.sleep(2)

        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div['
                                     '3]/div[5]/a/div/span/span').click()
        except:
            time.sleep(5)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div['
                                     '3]/div[5]/a/div/span/span').click()

        time.sleep(2)
        try:
            email = self.driver.find_element(By.CSS_SELECTOR,
                                             "#layers > div:nth-child(2) > div > div > div > div > div > "
                                             "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
            email.send_keys(TWITTER_EMAIL)
        except:
            time.sleep(15)
            email = self.driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > "
                                                              "div > "
                                                              "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
            email.click()
            email.send_keys(TWITTER_EMAIL)
        else:
            pass

        time.sleep(2)
        try:
            next = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
            next.click()
        except:
            time.sleep(5)
            next = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
            next.click()
        else:
            pass

        time.sleep(2)
        try:
            usr = self.driver.find_element(By.CSS_SELECTOR,
                                           "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
            usr.send_keys("pantha704")

        except:
            time.sleep(5)
            usr = self.driver.find_element(By.CSS_SELECTOR,
                                           "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
            usr.click()
            usr.send_keys("pantha704")
        else:
            pass

        time.sleep(2)
        try:
            next = self.driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > "
                                                             "div > "
                                                             "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > span > span")
            next.click()
        except:
            time.sleep(5)
            next = self.driver.find_element(By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > "
                                                             "div > "
                                                             "div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div > div > span > span")
            next.click()
        else:
            pass

        time.sleep(2)
        try:
            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                          '3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
        except:
            time.sleep(15)
            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                          '3]/div/label/div/div[2]/div[1]/input')
            password.click()
            password.send_keys(TWITTER_PASSWORD)
        else:
            pass

        time.sleep(2)
        try:
            log = self.driver.find_element(By.CSS_SELECTOR,
                                           "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div > span > span")
            log.click()
        except:
            time.sleep(5)
            log = self.driver.find_element(By.CSS_SELECTOR,
                                           "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div > span > span")
            log.click()
        else:
            pass

        time.sleep(2)
        try:
            text = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span")
            text.send_keys("Yo! this is a selenium webdriver typing this message for you.")

        except:
            time.sleep(5)
            text = self.driver.find_element(By.CSS_SELECTOR,
                                            "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span")
            text.send_keys("Yo! this is a selenium webdriver typing this message for you.")

        else:
            tweet = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div:nth-child(2) > div > div > span > span")
            tweet.click()

        time.sleep(15)


PROMISSED_UP = 40
PROMISSED_DOWN = 40
TWITTER_EMAIL = "pratham.jaiswal2004@gmail.com"
TWITTER_PASSWORD = "prathamj!"

chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chromedriver.exe"
service = Service(chrome_driver_path)

bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()

if float(speed[0]) < PROMISSED_DOWN or float(speed[1]) < PROMISSED_UP:
    bot.tweet_at_provider()
