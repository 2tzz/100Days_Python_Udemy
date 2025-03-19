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


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# word_list = sentence.split()

# print(word_list)

# result = {word:len(word)  for word in word_list}

# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = { day: int(celcius) * 9/5 +32 for (day, celcius) in weather_c.items()}

# print(weather_f)


student_dict = {
    "student" : ["Angela" , "James" , "Lilly"],
    "score"   : [56,76,98]
}

for (key,value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)


#loop through data frame

# for(key,value) in student_data_frame.items() :
#     print(value)


#loop through rows of a data frame

for (index , row) in student_data_frame.iterrows():
    print(row.score)