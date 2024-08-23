from selenium import webdriver

driver = webdriver.Chrome()

i = 0
while i < 1000:
    driver.get(url="https://github.com/pantha704")
    driver.implicitly_wait(5)
    i += 1
    print(i)


