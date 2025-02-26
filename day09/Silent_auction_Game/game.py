

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