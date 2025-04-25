from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_URL ="http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"
spotifi_URI = "spotify:track:6rqhFgbbKwnb9MLmUQDhG6"
spotify_ID = '6rqhFgbbKwnb9MLmUQDhG6' 

date = '2002-01-05'

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(URL , headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_tags = soup.find_all("h3", class_="a-no-trucate")

# Get clean text and remove extra whitespace
songs = [tag.get_text(strip=True) for tag in song_tags]

# Print only the first 100, in case more are found
print(songs)