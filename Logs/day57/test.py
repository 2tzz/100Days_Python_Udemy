
import requests

name = 'michel'
response = requests.get(url=f"https://api.agify.io/?{name}")
response.raise_for_status()
data = response.json()
guessing_age = data['age']

print(guessing_age)