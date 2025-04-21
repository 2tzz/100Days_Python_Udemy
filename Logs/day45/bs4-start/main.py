from bs4 import BeautifulSoup

path = "website.html"



with open(path) as html_file :
    html_content = html_file.read()

print(html_content)