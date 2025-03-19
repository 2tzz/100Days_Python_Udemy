# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")


letters = data["letter"].to_list()
codes = data["code"].to_list()



word_dic = dict(zip(letters , codes))




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter your word :").upper()

input_letter_list = list(user_input)



output_list = [word_dic[lt] for lt in input_letter_list]

print(output_list)




