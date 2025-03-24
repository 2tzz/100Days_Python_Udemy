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
list_is_true = True
data = pandas.read_csv("nato_phonetic_alphabet.csv")

letters = data["letter"].to_list()
codes = data["code"].to_list()

word_dic = dict(zip(letters , codes))


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



while list_is_true :

    user_input = input("Enter your word :").upper()
    input_letter_list = list(user_input)

    if user_input == 'EXIT':
        list_is_true = False

    
    else:
        try :
            
            output_list = [word_dic[lt] for lt in input_letter_list ]
        

        except KeyError:

            print("Please enter alphabet keys only")

        else:
            print(output_list)






