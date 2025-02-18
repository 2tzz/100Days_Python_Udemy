import random

# def is_prime(num):
#     temp1 = 0
#     temp2 = 0
#     for i in range(2,(num-1)) :

#         if num % 1 == 0 and num % num ==0:
#             temp1 += 1

#         if num % i == 0 :
#             temp2 += 1


#     if temp1 > 0 and temp2 == 0 :
#         return True
#     elif num == 2 :
#         return True

#     elif temp2 > 0 :
#         return False
    
         
# print (is_prime(2))

print("Welcome to number guessing game ")

numbers = []

for i in range (0 , 100) :
    numbers.append(i+1)

print(numbers)
guess = random.choice(numbers)


    
user_input = 0

while guess != user_input :

    user_input = int(input("Make a guess : "))

    if user_input == guess :
        print(f"you guess the number !! number was {guess}")

    elif user_input < guess :
        print("too low")

    elif user_input < guess :
        print("too high")






