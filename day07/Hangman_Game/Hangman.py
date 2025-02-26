
import random
from hangman_art import logo


#hangman game my implimentation 2tzz

words_list = ['apple','keyboard','phone','computer','moniter','programmer','bucket','allow','river']


chosen_word = random.choice(words_list)



word_len = len(chosen_word)



hang_count = 0
win_count = 0
try_count = 0

inc1 = 0
inc2 = 0

x = 0 
rec_list = []

for j in range(0,word_len):

    rec_list.append('_')

rec_word = ""
for k in rec_list :
    rec_word += k


print(logo)

print(rec_word)
    
while win_count < word_len and try_count < (win_count + 7) :
    guess = input("enter a character  : ").lower()

    

    for i in chosen_word :

        if i == guess:
            rec_list.pop(inc2)
            rec_list.insert(inc2 , i)
            win_count += 1
            inc2 += 1

        else:
            
            
            inc2 += 1

    try_count += 1



       


    if try_count == win_count + 1:
        print('''
        +---+
        |   |
            |
            |
            |
            |
        =========''')    

    elif try_count == win_count + 2 :
        print('''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''')    
        

    elif try_count == win_count + 3 :
        print('''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''')
    elif try_count == win_count + 4 :
        print('''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''')
    
    elif try_count == win_count + 5 :
        print( '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''')
    elif try_count == win_count + 6 :
        print('''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''')
        
    elif try_count == win_count + 7 :
        print('''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''')
        print ("you loose !")
        print (chosen_word , end="  ")
        print("Is the correct word")
    inc2 = 0

    rec_word = ""

    for k in rec_list :
        rec_word += k

    print(rec_word)


if chosen_word == rec_word :
    print ("you win !  !  ! ")
        