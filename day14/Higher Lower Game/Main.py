import random
from art import logo , vs
from game_data import data

temp = {}

temp = random.choice(data)

print(temp)

print(temp['name'])
print(temp['follower_count'])
print(temp['description'])
print(temp['country'])

