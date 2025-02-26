import random

print("hellow welcome to rock paper scissors game. ")

user_input = int(input("What do you want to choose ? type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_input = random.randint (0 , 2)



if user_input == 0 :
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")


elif user_input == 1 :
    print("""
            _______
        ---'    ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
        """)

elif user_input == 2 :
    print("""
            _______
        ---'   ____)____
                  ______)
              __________)
               (____)
        ---.__(___)

        """)

else :
    print("Wrong input")


print("Computer Input")


if computer_input == 0 :
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")


elif computer_input == 1 :
    print("""
            _______
        ---'    ____)____
                   ______)
                   _______)
                  _______)
         ---.__________)
        """)

elif computer_input == 2 :
    print("""
            _______
        ---'   ____)____
                  ______)
              __________)
               (____)
        ---.__(___)

        """)

else :
    print("Wrong  computer input")


if user_input == computer_input :
    print("draw")

elif user_input ==  0 and computer_input == 2:
    print("you win")

elif user_input == 0 and computer_input == 1:
    print("computer wins")

elif user_input == 1 and computer_input == 0 :
    print("you win")

elif user_input == 1 and computer_input == 2 :
    print("computer wins")

elif user_input == 2 and computer_input == 0 :
    print ("computer wins")

elif user_input ==2 and computer_input == 1 :
    print ("you win")

else :
    print ("error")