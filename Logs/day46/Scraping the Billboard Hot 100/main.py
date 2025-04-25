from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# Spotify credentials from .env
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")


# Spotify authentication ;]
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

USER_ID = sp.current_user()['id']

year = input("Enter year you want songs from :")
month = input("Enter month  :")
date = input("Enter date :")

date = f'{year}-{month}-{date}'

print(f"Adding a playlist with 100 top songs related to date - {date}")
# Date for Billboard chart
# date = '2010-12-31'


URL_BILL = f"https://www.billboard.com/charts/hot-100/{date}/"
header_bill = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

# Scrape Billboard chart
response = requests.get(URL_BILL, headers=header_bill)
soup = BeautifulSoup(response.text, "html.parser")

# Extract song names
song_tags = soup.find_all("h3", class_="a-no-trucate")
songs = [tag.get_text(strip=True) for tag in song_tags]

print("Top songs:", songs[:5])  # Just preview top 5 for now



# Create new playlist
playlist = sp.user_playlist_create(
    user=USER_ID,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top Billboard songs on {date}"
)

print("Created playlist:", playlist['name'])
print("Playlist URL:", playlist['external_urls']['spotify'])

track_uris = []
year = date.split("-")[0]

for song in songs:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query, type="track", limit=1)
    try:
        uri = result['tracks']['items'][0]['uri']
        track_uris.append(uri)
    except IndexError:
        print(f" Couldn't find track: {song}")

# Add tracks to the playlist (Spotify limits 100 per request)
if track_uris:
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    print(f"✅ Added {len(track_uris)} tracks to the playlist!")
else:
    print("⚠️ No tracks were added.")
