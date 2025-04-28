from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, "html.parser")

# Find the <strong> tag inside <p class="price">
price_tag = str(soup.select_one("span.aok-offscreen").text)

price =  float(price_tag.replace("$", ""))

print(price )


