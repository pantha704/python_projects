import requests, datetime as dt, time
from twilio.rest import Client

STOCK_URL = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "O9WZG07A2RSI958N"
NEWS_URL = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = "ff5620e8236f4a869b079fd399afbc74"
TWILIO_ACC_SID = "AC96949468a91c90bdf054e1c4f57f24c5"
TWILIO_AUTH_TOKEN = "bc890901bd1916565c8c65740b1e529a"
up_down = None
percent_diff = None

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def get_news():
    news_param = {
        "apiKey": f"{NEWS_API_KEY}",
        "qInTitle": f"{COMPANY_NAME}",
        "category": "business",
        "country": "us",
    }
    response = requests.get(f"{NEWS_URL}", params=news_param)
    response.raise_for_status()
    articles = response.json()['articles']
    first3articles = articles[:3]
    # print(first3articles)
    article_list = [f"\n{STOCK}: {up_down}{percent_diff}%\nHeading: {article['title']}\nBrief: {article['description']}"
                    for article in first3articles]
    print(article_list)
    send_message(article_list)


def get_stock():
    global up_down, percent_diff

    stock_param = {
        "function": "TIME_SERIES_DAILY",
        "symbol": f"{STOCK}",
        "apikey": f"{STOCK_API_KEY}",
    }
    # Time Series (Daily)
    response = requests.get(f"{STOCK_URL}", params=stock_param)
    response.raise_for_status()
    stock_yesterday = response.json()["Time Series (Daily)"][f"{yesterday}"]["4. close"]
    # print(stock_yesterday)
    stock_db4yest = response.json()["Time Series (Daily)"][f"{db4yest}"]["4. close"]
    print(stock_db4yest)
    difference = round(float(stock_yesterday) - float(stock_db4yest))
    # print(difference)
    percent_diff = round((difference / float(stock_yesterday)) * 100)
    # print(percent_diff)

    if percent_diff > 0:
        up_down = "UP 📈"
    else:
        up_down = "DOWN 📉"

    get_news()


def send_message(articles):
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(body=f"\n{article}", from_="+14847491772",
                                         to="+918582995868"
                                         )
        time.sleep(12)


today = dt.datetime.now().date()
print(today)
yesterday = today - dt.timedelta(days=1)
db4yest = yesterday - dt.timedelta(days=1)
print(yesterday)
get_stock()
