import requests
import smtplib
from email.message import EmailMessage

msg = EmailMessage()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_gmail = "testing.brainstrom@gmail.com"
my_password = "lotzylecosbwmpiu"

parameter1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": "CJE8ZGZF8PG8FW4V"
}

parameter2 = {
    "q": COMPANY_NAME,
    "from": "2026-09-16",
    "sortBy": "popularity",
    "apiKey": "ead2476047ad49969666daacdc838233"
}

response1 = requests.get("https://www.alphavantage.co/query", params=parameter1)
response1.raise_for_status()
data1 = float(response1.json()["Time Series (Daily)"]["2026-09-17"]["4. close"])
data2 = float(response1.json()["Time Series (Daily)"]["2026-09-16"]["4. close"])

percentage_change = ((data1-data2)/data2)*100


response2 = requests.get("https://newsapi.org/v2/everything", params=parameter2)
response2.raise_for_status()


if percentage_change > 1 or percentage_change < -1:
    title0 = response2.json()["articles"][0]["title"]
    content0 = response2.json()["articles"][0]["description"]

    title1 = response2.json()["articles"][1]["title"]
    content1 = response2.json()["articles"][1]["description"]

    title2 = response2.json()["articles"][2]["title"]
    content2 = response2.json()["articles"][2]["description"]

    msg["Subject"] = "Information from Stock News!"
    msg["From"] = my_gmail
    msg["To"] = "mauryaravishverma123@gmail.com"

    msg.set_content(
        f"Title: {title0}\n"
        f"Content: {content0}\n\n"
        f"Title: {title1}\n"
        f"Content: {content1}\n\n"
        f"Title: {title2}\n"
        f"Content: {content2}"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_password)
        connection.send_message(msg)


