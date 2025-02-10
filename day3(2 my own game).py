print("hey welcome to Race pit")
print('''      
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠿⠿⠿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⢀⡿⠟⠋⠁⠀⠀⠀⠀ ⠸⢿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠀⠀⣠⡴⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢀⣬⢯⣭⡉⠛⠻⢿⣿⣿⣿⡇
⣿⣇⣀⣸⡏⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢈⣷⠀⠀⠶⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣷⣶⣾⣿⣷⣶⣶⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')
input1 = input ("Wich tires do you want? fast, grip road or offroad ?").lower()

if input1 == 'fast' :

    print("your tire blown while driving offroad part you loose !")
elif input1 == 'offroad' :

    print("other cars faster than you ! you loose !")

elif input1 == 'grip' or 'road' :
    print("Congrads you took 1st place for frist part of the track")

    input2 = int(input("Enter what gear you want to choose for next off road part 1 ,2 ,3 ,4 :"))

    if input2 == 1 or 2 :
        print("congrads you took 1st place for 2nd part of the track race !!")

        input3 = int(input("you are entering last icy part of the track ! \n what speed u want to drive enter between 0 - 250  :"))

        if input3 <= 40 :
            print("nooo !  you are too sloww . You loose!")

        elif input3 <= 80 :
            print ("Congrads ! you won All the laps and Won the Race !")
            print('''
                     ___________
                    '._==_==_=_.'
                    .-\:      /-.
                   | (|:.     |) |
                    '-|:.     |-'
                      \::.    /
                       '::. .'
                         ) (
                       _.' '._
                      `"""""""`   ''')
        else :
            print("WRONG INPUT")

    elif input2 == 3 or 4 :
        print ("Nooo ! wrong gear you stuck on the mud . You loose!")

    else:
        print("Wrong input please enter 1 , 2, 3, 4")

else :

    print ("wrong input")    

