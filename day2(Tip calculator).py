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

input1 = input("oh there is a split on the roadway do you want to choose left or right ?")

if input1 == 'left':
    input2 = input("swim or wait ?")

    if input2 == 'wait':
        print("boat arrived and took you to an island")
        
        input3 = input("there are three doors blue , red and yellow wich one u choose?")

        if input3 == 'yellow':
            print("⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶ You win you found the treasure ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶")

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