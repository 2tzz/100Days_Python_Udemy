import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

# Write your code below this line 👇

soup = BeautifulSoup(response.text , "html.parser")

movies = soup.find_all("h3")
movie_names = [movie.get_text() for movie in movies]
movie_names.reverse()
print(movie_names)


for mov in movie_names :

    text = f"{mov} \n"
   
   
    new_text =  text.replace(")" , ".")
    print(new_text)
    
    with open ("movie_names.text" , mode="a") as file :
        try :
            file_contents = file.write(new_text)
        except :
            file_contents = file.write("unicode - error \n")








