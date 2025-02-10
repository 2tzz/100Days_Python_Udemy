# mystry = 734_529.678


# print(type(mystry))






# print("number of letters in your name :" , len(input("enter your name here")) )



# bmi = 83 / 1.65  ** 2 
# print(round(bmi,2))



# score = 0
# height = 1.8

# is_winning = True

# print(f"your score is = {score}  yor height is = {height}  are you winning = {is_winning}")
# x = int(input("Enter your total  bill : "))

# print(f"your total bill is : {x} $")
# y = int(input("enter how  much persentage of tip u give (10%,15%,20%):"))

# total = x +  x / 100 * y


# print(f"yor total will be : {total} $")

# #

print("Welcome to treasure island")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

input1 = input("oh there is a split on the roadway do you want to choose left or right ?").lower()

if input1 == 'left':
    input2 = input("swim or wait ?").lower()

    if input2 == 'wait':
        print("boat arrived and took you to an island")
        
        input3 = input("there are three doors blue , red and yellow wich one u choose?").lower()

        if input3 == 'yellow':
            print("⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶ You win you found the treasure ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶")

            print('''
                       ''')

        elif input3 == 'blue':
            print("eaten by beasts.game over.")

        elif input3 == 'red':
            print("room full of fire.Game over")

        else :
            print("wrong input")


    elif input2 == 'swim':
        print("Attaked by trout Gamer over")
    else:
        print("wrong input")
else :
    print("Fall in to a hall game over")