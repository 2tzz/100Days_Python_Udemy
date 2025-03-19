import random

# # numbers = [1 , 2 , 3]

# # new_numbers = [ item+1 for item in numbers]

# # print(new_numbers)


# # doubledlist = [item * 2 for item in range(1,5)]

# # print(doubledlist)

# names = ["Alex" , "beth" , "Carloline" ,  "Dave" , "Elanor" , "Freddie"]

# # converted_list = [item.upper() for item in names]

# # print(converted_list)


# student_scores = {student:random.randint(1,100) for student in names}


# passed_students = {student:score for (student , score) in student_scores.items() if score >= 60 }

# print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_list = sentence.split()

print(word_list)

result = {word:len(word)  for word in word_list}

print(result)