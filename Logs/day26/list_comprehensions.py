numbers = [1 , 2 , 3]

new_numbers = [ item+1 for item in numbers]

print(new_numbers)


doubledlist = [item * 2 for item in range(1,5)]

print(doubledlist)

names = ["Alex" , "beth" , "Carloline" ,  "Dave" , "Elanor" , "Freddie"]

converted_list = [item.upper() for item in names]

print(converted_list)