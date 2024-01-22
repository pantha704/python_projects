#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="pratham.jaiswal2004@gmail.com", msg="This is a Test Email.")
import random
import smtplib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# import datetime as dt

my_email = "prathamjaiswal204@gmail.com"
password = "rhhxzirrnqoisxbi"
reciever = "prathamjaiswal204@gmail.com"

word_list = ["Fresh", "Super", "Amazing", "Fantastic", "Enthusiastic", "Optimistic", "Positive", "Bright", "Awakening",
             "Rejuvenating", "Energizing", "Enlivening", "Invigorating"]


def tweet_at_provider(msg):
    chrome_driver_path = r"C:\Users\prath\OneDrive\Desktop\udemy\python dev\chromedriver_win32\chrome.exe"
    driver = webdriver.Chrome()

    driver.implicitly_wait(15)
    driver.get(url="https://x.com/login")

    driver.implicitly_wait(15)
    email = driver.find_element(By.XPATH,
                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    email.send_keys("pantha704")
    # print("try block")

    driver.implicitly_wait(15)
    next = driver.find_element(By.XPATH,
                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
    next.click()

    driver.implicitly_wait(15)
    password = driver.find_element(By.XPATH,
                                   '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.click()
    password.send_keys("prathamj!")
    password.send_keys(Keys.ENTER)

    driver.implicitly_wait(15)
    text = driver.find_element(By.CSS_SELECTOR,
                               '#react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')

    # #react-root > div > div > div.css-175oi2r.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div.css-175oi2r.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div

    text.click()
    text.send_keys(
        f"{msg}")

    driver.implicitly_wait(15)
    tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                          '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                          '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div['
                                          '3]/div/span/span')
    tweet.click()
    print("Posted! :)")
    time.sleep(15)


with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    try:
        with open("count.txt", mode="r+") as count:
            quote_count = int(count.read())
            # print("Day:", quote_count)
    except:
        with open("count.txt", mode="w") as count:
            count.write("0")

    finally:
        with open("count.txt", mode="r+") as count:
            quote_count = int(count.read())
            # print("Day:", quote_count)

        with open("count.txt", mode="w") as count:
            if quote_count < len(all_quotes) - 1:
                count.write(str(quote_count + 1))
                quote = f"Day: {quote_count}\n\n{all_quotes[quote_count]}"
            else:
                count.write(str(0))
                quote = (f"\n{all_quotes[quote_count]}\n\nWell done! It's Day {quote_count}. Restarting from "
                         f"tomorrow ;)")
        print(quote)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(from_addr=my_email, to_addrs=reciever,
        #                         msg=f"Subject: Your {random.choice(word_list)} Morning Starter!\n\n{quote}")
        #     connection.close()


with open("quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    try:
        with open("tweet_day.txt", mode="r+") as count:
            tweet_count = int(count.read())
            # print("Day:", quote_count)
    except:
        with open("tweet_day.txt", mode="w") as count:
            count.write("0")

    finally:
        with open("tweet_day.txt", mode="r+") as count:
            tweet_count = int(count.read())
        with open("tweet_day.txt", mode="w") as count:
            count.write(str(tweet_count + 1))
            # print("Day:", quote_count)

        msg = f"#Day{tweet_count} of coding\n{all_quotes[tweet_count]}"
        tweet_at_provider(msg=msg)
        print(f"{msg}")

