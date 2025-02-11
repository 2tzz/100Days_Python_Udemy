
import random

words_list = ['apple','keyboard','phone','computer','moniter','programmer','bucket','allow','river']


chosen_word = random.choice(words_list)

print(chosen_word)

word_len = len(chosen_word)

guess = input("enter a character  : ").lower()

for i in chosen_word :

    if i == guess:
        print("correct", end= "  ")

    else:
        print("wrong",end="  ")