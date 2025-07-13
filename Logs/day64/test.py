import requests

movie_name = 'Harry Potter    '

new_movie = movie_name.replace(' ','+')


url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTRjMDI0Yzg2ODc4ZTFlYWM1M2UxODZmNWM2ZDM3MyIsIm5iZiI6MTc1MjMyNzE3Ni44MjcwMDAxLCJzdWIiOiI2ODcyNjQwODkxOTUxN2FjZTlhOTgwYjciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.7z7aPFPHy_0egG6yaJfOa7_WBVkFi02Gdl4PSc_-Kiw"
}

response = requests.get(url, headers=headers)
data = response.json()

for item in data['results'] :
    print (item['original_title'])