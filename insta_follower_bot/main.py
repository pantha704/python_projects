from insta_bot import InstaFollower

# def get_element(method, path):
#     try:
#         element = driver.find_element(f'By.{method},{path}')
#         return element
#     except:
#         time.sleep(5)
#         element = driver.find_element(f'By.{method},{path}')
#         return element
#     finally:
#         get_element(method, path)


similar_acc = "iamsrk"
USERNAME = "pantherr.in"
PASSWORD = "prathamj!?"

bot = InstaFollower()
bot.login(username=USERNAME, passwd=PASSWORD)
bot.find_and_follow(name=similar_acc)

while True:
    bot.following()
