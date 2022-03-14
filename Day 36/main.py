import requests
from twilio.rest import Client

STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'QYQH9HHUP28AYAAM'

stock_parameter = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()

data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing = float(data_list[0]['4. close'])
day_before_yesterday_closing = float(data_list[1]['4. close'])

difference = day_before_yesterday_closing - yesterday_closing
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

diff_percent = round((difference / yesterday_closing) * 100, 2)

if abs(diff_percent) > 4:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
    NEWS_API_KEY = '3fd9eaa502c34190b315c92d0ee6f482'

    news_parameter = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_response.raise_for_status()

    articles = news_response.json()["articles"][:3]
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    foramtted = [
        f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}, \nBrief: {article['description']}" for article in articles]

    TWILIO_SID = 'AC8a2f8b00db295548bc94aa23a7ffe34b'
    TWILIO_AUTH = 'bad23e6676b66fbc6f42723cd9f7ada1'
    MY_NO = '+19107271760'

    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in foramtted:
        message = client.messages \
                        .create(
                            body=article,
                            from_=MY_NO,
                            to='+917978133655'
                        )

        print(message.status)
