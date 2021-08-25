import requests
import os
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"



stock_base_url = 'https://www.alphavantage.co/query?'
api_key = os.environ.get('API_K')
news_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': api_key,
}

response = requests.get(stock_base_url, params=news_params)
stock_data = response.json()["Time Series (Daily)"]

stock_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_list[0]
day_before_yesterday_data = stock_list[1]
yesterday_closing_price = float (yesterday_data['4. close'])
before_yesterday_price = float(day_before_yesterday_data['4. close'])

print(yesterday_closing_price)
print(before_yesterday_price)



today_date = datetime.today().strftime('%Y-%m-%d')
news_api_key = os.environ.get('NEWS_API_K')
news_base_url = 'https://newsapi.org/v2/everything?'
news_params = {
    'q': 'Tesla',
    'from':today_date,
    'sortBy': 'popularity',
    'apiKey': news_api_key
}

news_response = requests.get(news_base_url, params=news_params)
news_data = news_response.json()
latest_three = news_data['articles'][:2]


def compare_price(current, previous):
    if current == previous:
        return 0
    try:
        diff_percentage = (abs(current - previous) / previous) * 100.0
        if diff_percentage > 1:
            return latest_three
    except ZeroDivisionError:
        return 0

compare_price(yesterday_closing_price, before_yesterday_price)


