
import random

cards = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []
plyer_total = 0
dealer_total = 0
temp = 0
condition = ''

player_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
dealer_cards.append(random.choice(cards))

print(f"your cards  : {player_cards}")
print(f"Dealer cards  : {dealer_cards}")

condition = input("Do you want to add another card ? type 'y' for yes 'n' for no")

if condition == 'y':
    player_cards.append(random.choice(cards))

    plyer_total = sum(player_cards)
    print(f"your cards  : {player_cards}")
    print(plyer_total)

    dealer_cards.append(random.choice(cards))
    print(f"Dealer cards  : {dealer_cards}")
    dealer_total = sum(dealer_cards)
    print(dealer_total)




