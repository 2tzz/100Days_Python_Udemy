import random
from art import logo , vs
from game_data import data

vs1i = 0
vs1s = ''
vs2i = 0
vs2s = ''
x = 0
score =  0



def rand_item(dic):

    temp = {}
    f_count = 0

    temp = random.choice(dic)
    f_count = int(temp['follower_count'])
  

    return f_count ,  f"{temp['name']} is a {temp['description']} from {temp['country']} ."


vs1i , vs1s = rand_item(data)

vs2i , vs2s = rand_item(data)


print (" Welcome to higher lover game  !!!!")
print(logo)

print ("A : " , vs1s)

print(vs)

print("B : " , vs2s)

user_input = input("Wich one has more followers  enter 'A' or 'B'  : ")


if user_input == 'A' :

    if vs1i > vs2i :

        print("you are correct !!")
        score += 1

    else :
        print("Sorry u are wrong")

elif  user_input == 'B':

    if vs2i > vs1i :

        print("you are correct !!")
        score += 1
    else :
        print("Sorry u are wrong")







