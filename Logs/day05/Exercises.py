fruits = ['apple','peach','pear']

for fruit in fruits:
    print (fruit)

student_scores = [150 , 142 , 185 , 120 , 171 , 184 , 149 , 24 , 59 , 68 , 199 , 78 , 65 , 89 , 86 ]

max_score = 0

for i in student_scores :


    if i > max_score :
        max_score = i


print ("max score : " , max_score)

for number in range(1 , 10 , 2):
    print(number)

# challenge 1

sum = 0

for num in range (1,101):
    
    sum = sum + num

print(sum)

# challenge 2 ez

for num in range(1,101):
    
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    
    elif num % 3 == 0 :
        print("Fizz") 
        
    elif num % 5 == 0 :
        print("Buzz")
        
    else:
        print (num)
