# from bs4 import BeautifulSoup
# import lxml
# import requests


# path = "website.html"

# response = requests.get("https://news.ycombinator.com/news")
# yc_web = response.text

# # with open(path) as html_file :
# #     html_content = html_file.read()

# soup = BeautifulSoup(yc_web , "html.parser")

# print(yc_web)


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store the results
titles = []
links = []
upvotes = []
upvote_int = []

# Each post is in a <tr class="athing">
articles = soup.select("tr.athing")

for article in articles[:30]:  # First 30 articles
    # Title and link
    title_tag = article.select_one("span.titleline a")
    title = title_tag.get_text() if title_tag else "N/A"
    link = title_tag['href'] if title_tag else "N/A"

    # Upvotes are in the next <tr> row under <span class="score">
    subtext = article.find_next_sibling("tr")
    score_tag = subtext.select_one("span.score")
    score = score_tag.get_text() if score_tag else "0 points"
    new_score  = int(score.split()[0])
    # Append to lists
    titles.append(title)
    links.append(link)
    upvotes.append(new_score)


# Print to check
# print("Titles:", titles)
# print("Links:", links)
print("Upvotes:", upvotes)

max_value = max(upvotes)
max_index = upvotes.index(max_value)
print(max_value , max_index)
    
print (f"Title : {titles[max_index]} , Link : {links[max_index]} , Upvotes : {max_value}")