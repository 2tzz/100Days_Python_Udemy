
import random
# fruits = ['apple','peach','pear']

# for fruit in fruits:
#     print (fruit)

# student_scores = [150 , 142 , 185 , 120 , 171 , 184 , 149 , 24 , 59 , 68 , 199 , 78 , 65 , 89 , 86 ]

# max_score = 0

# for i in student_scores :


#     if i > max_score :
#         max_score = i


# print ("max score : " , max_score)

# for number in range(1 , 10 , 2):
#     print(number)

#challenge 1

# sum = 0

# for num in range (1,101):
    
#     sum = sum + num

# print(sum)

#challenge 2 ez

# for num in range(1,101):
    
#     if num % 3 == 0 and num % 5 == 0:
#         print ("FizzBuzz")
    
#     elif num % 3 == 0 :
#         print("Fizz") 
        
#     elif num % 5 == 0 :
#         print("Buzz")
        
#     else:
#         print (num)


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','Z','X']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','+']


print ("Welcome to pasword Generator !")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password ?\n"))
nr_numbers = int(input("How many numbers do you want in your password ?\n"))


# print("Your ez  password is : ",end="")


# for i in range(0,nr_letters) :

#     print(random.choice(letters),end="")

# for i in range(0,nr_symbols) :

#     print(random.choice(symbols),end="")


# for i in range(0,nr_numbers) :

#     print(random.choice(numbers),end="")


print("Your hard  password is : ",end="")



letter_count = 0
symbol_count = 0
number_count = 0



while (letter_count + symbol_count + number_count) < (nr_letters + nr_symbols +nr_numbers):

    

    x = random.randint(0 , 3)

    if x == 0 and nr_letters  >  letter_count:
        print(random.choice(letters),end="")
        letter_count += 1

    elif x == 1 and symbol_count < nr_symbols :
        print(random.choice(symbols),end="")
        symbol_count += 1

    elif x == 2 and number_count < nr_numbers :
        print(random.choice(numbers),end="")
        number_count += 1
    

#hard challenge done ;]

#hard challenge another way

password_list = []



print("     Your hard type 2  password is : ",end="")


for i in range(0,nr_letters) :

    password_list.append(random.choice(letters))

for i in range(0,nr_symbols) :

    password_list.append(random.choice(symbols))


for i in range(0,nr_numbers) :

    password_list.append(random.choice(numbers))


random.shuffle(password_list)

password = ""

for char in password_list :
    password += char

print(password)













