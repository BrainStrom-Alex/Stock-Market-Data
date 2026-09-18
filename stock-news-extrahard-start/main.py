import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameter1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": "CJE8ZGZF8PG8FW4V"
}

parameter2 = {
    "q": COMPANY_NAME,
    "from": "2026-09-15",
    "sortBy": "publishedAt",
    "apiKey": "ead2476047ad49969666daacdc838233"
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query", params=parameter1)
response.raise_for_status()
data1 = float(response.json()["Time Series (Daily)"]["2026-09-17"]["4. close"])
data2 = float(response.json()["Time Series (Daily)"]["2026-09-16"]["4. close"])

percentage_change = ((data1-data2)/data2)*100

if percentage_change > 1 or percentage_change < -1:
    print("Get Data")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response1 = requests.get("https://newsapi.org/v2/everything", params=parameter2)
response1.raise_for_status()
data1 = response1.json()["articles"]
print(data1)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

