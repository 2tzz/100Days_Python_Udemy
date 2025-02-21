# my_dictionary = {"bug" : "thiyura" , "cug" : "heshadi" , "fug" : "tootee"}

# print(my_dictionary["bug"])

# my_dictionary["bug"] = 'thilakshana'

# print(my_dictionary)

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for i in student_scores :
    
    
#     if 100 >= student_scores[i] >90 :
#         student_scores[i] = 'Outstanding'
        
#     elif student_scores[i] > 80:
#         student_scores[i] = 'Exceeds Expectations'
        
#     elif student_scores[i] >70:c
#         student_scores[i] = 'Acceptable'
    
#     elif student_scores[i] <= 70 :
#         student_scores[i] = 'Fail'
        
# student_grades = student_scores.copy()
    
# print(student_grades)



# travel_log = {
#     "France": ["paris","Lille","Dijon"],
#     "Germany" : ["Stuttgart","Berlin"],
# }

# print(travel_log["France"][1])

# nesterd_list = ["A" , "B" , ["C" , "D"]]

# print(nesterd_list[2][0])


# travel_log = {
#     "France": {
#        "cities_visited" : ["Paris" , "Lille" , "Dijon"] ,
#        "total_visits" : 12
#     },
#     "Germany" : {
#         "cities_visited" : ["Berlin" , "Hamburg" , "Stuttgart"],
#         "total_visits" : 5
#     }
# }


# print(travel_log["Germany"]["cities_visited"][2])


# if bidders == 'yes':

#     cont += 1

# while bidders != 'no':

#     name = input("What is your name ?")

#     bid = input("what is yor bid ? : $")

#     bidders = input("Is there any bidders type 'yes' or 'no' :")

#     bidder_info[name] = bid_list[bid]

#     print(bidder_info)
        


############################### totezz ###########################

bidder_info = {}
cont = 0
bid_list = []

print("welcome to secreat auction program ! ")


print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________
      ''')

bidders = 'yes'



while bidders == 'yes'  :

    

    name = input("What is your name ?").lower()

    bid = int(input("what is yor bid ? : $"))

    bidders = input("Is there any bidders type 'yes' or 'no' :").lower()

    bidder_info[name] = bid

    print(bidder_info)

def find_highest_biddder(bidder_dic):
    highest_bid = 0
    winner = ""
    for bidder in bidder_dic:
        bid_amount = bidder_dic[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner}  with a bid of ${highest_bid}")




find_highest_biddder(bidder_info)
########################