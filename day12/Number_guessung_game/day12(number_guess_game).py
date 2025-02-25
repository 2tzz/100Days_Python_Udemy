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


################## NUmber guessing game my implementation ####################################

print("======= ===== ==== Welcome to number guessing game ===== ==== =======")

print("""                                                                                                                                        

  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
\n""")

numbers = []

for i in range (0 , 100) :
    numbers.append(i+1)


guess = random.choice(numbers)

    
def high_low(guessx,user_input) :
    ###prints high or low or the answere is correct
    # according to given guess###
    


    if user_input == guessx :
        return 0               
        
        
    elif user_input < guessx :
        return 1                                                  
        

    elif user_input > guessx :
        return 2                                                  
        
        

    

difficulty = input("\n What difficulty you want to paly with 'hard' or 'easy' type  : ")  

if difficulty == 'hard' :
    count = 0
    p = 0
    print("\n You have 5 attemts to complete this challenge \n")
    while p == 0 and count < 5:


        userinputx = int(input("Enter your guessing number : "))

        if high_low(guess , userinputx) == 0:
            print("attempt ", (5-count) )
            print(f"you guess the number !! number was {guess}")
            p += 5
            

        elif high_low(guess , userinputx) == 1 :
            print("attempt ", (5-count) )
            print("too low")
        
        elif high_low(guess , userinputx) == 2 :
            print("attempt ", (5-count) )
            print("too high")

        count += 1
        
elif difficulty == 'easy' :
    count1 = 0
    p1 = 0

    print("\n You have 10 attemts to complete this challenge \n")
    while p1 == 0 and count1 < 10:


        userinputx = int(input("Enter your guessing number : "))

        if high_low(guess , userinputx) == 0:
            print("attempt ", (10-count1) )
            print(f"you guess the number !! number was {guess}")
            p1 += 5
            

        elif high_low(guess , userinputx) == 1 :
            print("attempt ", (10-count1) )
            print("too low")
        
        elif high_low(guess , userinputx) == 2 :
            print("attempt ", (10-count1) )
            print("too high")

        count1 += 1




        




