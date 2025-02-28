import random
from art import logo , vs
from game_data import data

vs1i = 0
vs1s = ''
vs2i = 0
vs2s = ''
x = 0
score =  0
game_over = True

str_change = ''
int_change = 0



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



while game_over == True :

    
    
    user_input = input("Wich one has more followers  enter 'A' or 'B'  : ")

    print(f"your score {score}")

    if user_input == 'A' :

        if vs1i > vs2i :
            vs2i , vs2s = rand_item(data)
            print("you are correct !!")
            
            score += 1

            print ("A : " , vs1s)

            print(vs)

            print("B : " , vs2s)



        else :
            print("Sorry u are wrong")
            
            game_over = False

    elif  user_input == 'B':

        if vs2i > vs1i :
            
            print("you are correct !!")
            
            score += 1

            vs1i = int_change
            vs1i = vs2i
            vs2i = int_change

            vs1s = str_change
            vs1s = vs2s
            vs2s = str_change

            vs2i , vs2s = rand_item(data)

            print ("A : " , vs1s)

            print(vs)

            print("B : " , vs2s)




        else :
            print("Sorry u are wrong")

            
            game_over = False


#program completed by tooteezz




