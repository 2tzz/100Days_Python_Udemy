from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

my_email = os.getenv("MY_EMAIL")
passkey  = os.getenv("PASSKEY")


URL ="https://appbrewery.github.io/instant_pot/"
SEARCHING_PRICE =   100.0 

header = {"headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "httpbin.org",
            "Priority": "u=0, i",
            "Sec-Ch-Ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-68105be7-5416f1a359282ce2525f3e0c"}
        }


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


price_tag = str(soup.select_one("span.aok-offscreen").text)

price =  float(price_tag.replace("$", ""))



if price < SEARCHING_PRICE :
    with smtplib.SMTP("smtp.gmail.com") as connection :
                connection.starttls()  #transport layer security
                connection.login(user=my_email ,password=passkey)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs=f"tthiyura@gmail.com",
                    msg=f"Subject:your item price drop below {SEARCHING_PRICE} $ ! \n\n visit :  {URL}")


