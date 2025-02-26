# print("welcome to roller coster !")
# height = int(input("Enter your height : "))


# if height >=  120 :
#     print(" you can ride the rollercoster")

#     age =  int(input("Enter your age : "))


#     bill = 0

#     if age <= 12:
#         print("please pay 5 $")
#         bill = 5
#     elif age <= 18:
#         print("please pay 7 $")
#         bill = 7
#     else :
#         print("please pay 12 $")
#         bill = 12

#     pic = input("do you want a photo?")

#     if pic == 'yes' and age <= 12:
#             bill = bill + 3
#             print(f"yor total will be  : {bill} $")
    
#     else:
#           print(f"please pay the total : {bill} $ ")

# else :
#     print("sorry you can't ride this get taller to ride this")


print("welcome to python pizza Delivers!")

size = input ("what size piza do you want  Small - S Medium - M  Large - L (plese enter a character)  :")

pepperoni = input ("Do you want peperoni on top your pizza Y or N ?")

extra_cheese  = input("Do you want extra cheese on top Y or N ?")

total = 0

if size == 'S' :
    total = total + 15

elif size == 'M':
    total = total + 20

elif size == 'L':
    total = total + 25
    

if pepperoni == 'Y' and size == 'S' :

    total = total + 2

elif pepperoni == 'Y' and (size == 'M' or size == 'L' ):

    total = total + 3

if extra_cheese == 'Y' :

    total = total + 1

print(f"yor total will be {total}$")
#hhh










