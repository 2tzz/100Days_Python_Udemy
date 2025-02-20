#learning debugging

# from random import randint

# dice_images = ["0" , "0" , "0" , "0", "0" ,"0"]

# dice_num = 6
# print(dice_images[dice_num])

###########################################

# year = int(input("What is your year of birth : "))

# if 1980 < year <= 1994 :
#     print("You are Millenial")

# elif  1994 < year :
#     print("you are Gen Z")

################################################

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
    

# print(odd_or_even(11))

##################################################

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         # else:
#         #     return True
#     # else:
#     #     return False

# print(is_leap(2018))


#########################################################

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(20)

##########################################