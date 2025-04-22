# from bs4 import BeautifulSoup
# import lxml
# import requests
# import pprint

# path = "website.html"

# response = requests.get("https://news.ycombinator.com/news")
# yc_web = response.text

# # with open(path) as html_file :
# #     html_content = html_file.read()


# soup = BeautifulSoup(yc_web , "html.parser")

# artical_tags = soup.select("tbody")

# print(artical_tags)


from bs4 import BeautifulSoup
import requests

article_texts = []
article_links = []


response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

# Select all anchor tags inside titleline span
article_tags = soup.select("span.titleline a")

# Print the full anchor tags (first 30)
for tag in article_tags[:30]:
    # print(str(tag))
    links = tag.get("href")
    article_links.append(links)

