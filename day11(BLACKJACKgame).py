#my implementation



import random

cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []
plyer_total = 0
dealer_total = 0
temp = 0
condition = ''

cont = input("Do you want to play BLACKJACK ? 'y' or 'n' ? ")




while cont == 'y' :


    print('''
                 _     _            _    _            _    
                | |   | |          | |  (_)          | |                
                | |__ | | __ _  ___| | ___  __ _  ___| | __
                | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                | |_) | | (_| | (__|   <| | (_| | (__|   < 
                |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
                                       _/ |                
                                      |__/  

                     _____
                    |A .  | _____
                    | /.\ ||A ^  | _____
                    |(_._)|| / \ ||A _  | _____
                    |  |  || \ / || ( ) ||A_ _ |
                    |____V||  .  ||(_'_)||( v )|
                           |____V||  |  || \ / |
                                  |____V||  .  |
                                         |____V|                        ''')
    




    print("======================== NEW GAME ======================")

    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    print(f"your cards  : {player_cards}")
    print(f"Dealer cards  : {dealer_cards}")

    condition = input("Do you want to add another card ? type 'y' for yes 'n' for no   : ")

    if condition == 'y':

        player_cards.append(random.choice(cards))
        
        plyer_total = sum(player_cards)

        print(f" Your cards - {player_cards} ")
        

        dealer_cards.append(random.choice(cards))
        print(f" dealer cards - {dealer_cards} ")
        
        if plyer_total > 21 :
            print("\nYou loose\n\n")
            
        
        elif dealer_total < random.randint(13, 15):
            print("** Dealer pulls another card **")
            dealer_cards.append(random.choice(cards))
            print(f" dealer cards - {dealer_cards} ")
            plyer_total = sum(player_cards)
            dealer_total = sum(dealer_cards)

            if dealer_total > 21 or dealer_total < plyer_total :
                print("\nCongrads !! you Win !!\n\n")    

    elif condition == 'n':
        
        print(f" Your cards - {player_cards} ")
        

        dealer_cards.append(random.choice(cards))
        print(f" dealer cards - {dealer_cards} ")
        
        if plyer_total > 21 :
            print("\nYou loose\n\n")

        elif dealer_total < random.randint(10, 13):
            print("** Dealer pulls another card **")
            dealer_cards.append(random.choice(cards))
            print(f" dealer cards - {dealer_cards} ")
            plyer_total = sum(player_cards)
            dealer_total = sum(dealer_cards)


            if dealer_total > 21 or dealer_total < plyer_total :
                print("\nCongrads !! you Win\n\n !!")

    player_cards.clear()    
    dealer_cards.clear()
    plyer_total = 0
    dealer_total = 0
    temp = 0   

    #0343146479