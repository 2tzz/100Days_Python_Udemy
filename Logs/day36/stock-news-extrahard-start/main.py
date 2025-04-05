import requests
from datetime import datetime , timedelta
from twilio.rest import Client

STOCK = "TSCO.LON"
COMPANY_NAME = "Tesla Inc"
API_KEY_ALPHA   = "XXXXXXXX"
# pld alpha "SUP3IGRJNMY2R3WM" "8FJ89HHLOXFP6YQ0" 
API_KEY_NEWS = "XXXXXXXX"
API_ENDPOINT_ALPHA = "https://www.alphavantage.co/query"
API_ENDPOINT_NEWS = "https://newsapi.org/v2/everything"
TOKEN = "XXXXXXXX"
trade_list = []

today = datetime.now()
yesterday = str(datetime.now() - timedelta(1))
dbyesterday = str(datetime.now() - timedelta(2))

ys = yesterday.split(" ")
db = dbyesterday.split(" ")
yesterdays = ys[0] 
dbyesterdays = db[0]
 
print(yesterdays , dbyesterdays)



# datetime.strftime(yesterday, '%Y-%m-%d')
# '2015-05-26'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

trade_params = {
    "function": "TIME_SERIES_DAILY" ,
    "symbol" : STOCK,
    "interval" : "5min" ,
    "apikey" : API_KEY_ALPHA,

}

news_params = {
    "q" : "apple",
    "from" : dbyesterdays ,
    "to"   : yesterdays ,
    "sortBy" : "popularity",
    "apikey" : API_KEY_NEWS,
}




response_nws = requests.get(API_ENDPOINT_NEWS, params=news_params)
response_nws.raise_for_status()
news_data = response_nws.json()

news_list= news_data["articles"]
news_title = str(news_list[0]["title"])
popular_news = str(news_list[0]["description"])

response_alp = requests.get(API_ENDPOINT_ALPHA, params=trade_params)
response_alp.raise_for_status()
trade_data = response_alp.json()


trade_list= list(trade_data["Time Series (Daily)"].values())
yest_close = float(trade_list[0]["4. close"])
dbyest_close = float(trade_list[1]["4. close"])

# 4test
# yest_close = 390.0000

# dbyest_close = 360.0000


difference = yest_close - dbyest_close

if difference > 0 :

    msg = f"SLA: 🔺 {abs(round(difference / yest_close * 100))} %\nHeadline:{news_title}.\nBrief:{popular_news}"

elif difference < 0 :

    msg = f"SLA: 🔻 {abs(round(difference / yest_close * 100))} %\nHeadline:{news_title}.\nBrief:{popular_news}"

elif difference == 0  :

    msg = f"SLA: = {abs(round(difference / yest_close * 100))} %\nHeadline:{news_title}.\nBrief:{popular_news}"



account_sid = 'AC6b135ecffd98acf47e1f73b737990276'
auth_token = 'XXXXXXXX'
client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='+14028258539',
  body='hey',
  to='+94712835711'
)


