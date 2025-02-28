from art import logo

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


order_details = {}
remaining_resorces = {}
cofee_price = 0
total = 0



def cofee_details(cus_choice):

    order = {}
    price = 0

    if cus_choice == 'espresso':
        order = menu["espresso"]["ingredients"]
        price = menu["espresso"]["cost"]

        return order , price


    elif  cus_choice == 'latte':
        order = menu["latte"]["ingredients"]
        price = menu["latte"]["cost"]

        return order , price


    elif  cus_choice == 'cappuccino':
        order = menu["cappuccino"]["ingredients"]
        price = menu["lcappuccino"]["cost"]

        return order , price

    elif cus_choice == 'cancel' :
         
         print("Have a nice day !")

         return order , price

    else:
        print("Error")

        return order , price

def calc_coins(quarters ,dimes ,nickles ,pennies ):

        return float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)

#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

def calc_cofee (resources , input_resorces , input_price  , item_price , orderx):

    change = 0

    if orderx != 'espresso':
        resources["water"] = resources["water"] - input_resorces["water"]
        resources["milk"] = resources["milk"] - input_resorces["milk"]
        resources["coffee"] = resources["coffee"] - input_resorces["coffee"]
    elif orderx == 'espresso':
        resources["water"] = resources["water"] - input_resorces["water"]
        resources["coffee"] = resources["coffee"] - input_resorces["coffee"]

    change = input_price - item_price

    return change , resources

cofee_price = 0
total = 0

print(logo)

order = input("What kind of cofee do you need ? type (espresso/latte/cappuccino) : ")

order_details , cofee_price =  cofee_details(order)


print(f"{order}  will be {cofee_price}$  plese  enter coins below \n")

quarters = float(input("put quaters  here : "))
dimes = float(input("put dimes  here : "))
nickles = float(input("put nickles  here : "))
pennies = float(input("put pennies  here : "))

total = calc_coins(quarters ,dimes ,nickles ,pennies )

print(total)

change , remaining_resorces = calc_cofee(resources , order_details ,total , cofee_price , order)

print ( f" Here take the change {round(change, 2 )}$  Enjoy your {order} !!!")


condition = input("Do you want another coffee  type 'y' or 'n'  too check reamainings type 'r' : ")



while condition == 'y' or condition == 'r'  and order != 'cancel' :

    if condition == 'r' :
            print(f"Water: {remaining_resorces["water"]}  \n milk : {remaining_resorces["milk"]} \n coffee : {remaining_resorces["coffee"]} \n")

    order = input("What kind of cofee do you need ? type (espresso/latte/cappuccino) type 'cancel'  to end order process : ")

    if int(remaining_resorces["water"]) > 0 and  int(remaining_resorces["milk"]) > 0 and int(remaining_resorces["coffee"]) >0  and order != 'cancel':

        cofee_price = 0
        total = 0

        order_details , cofee_price =  cofee_details(order)


        print(f"{order}  will be {cofee_price}$  plese  enter coins below \n")

        quarters = float(input("put quaters  here : "))
        dimes = float(input("put dimes  here : "))
        nickles = float(input("put nickles  here : "))
        pennies = float(input("put pennies  here : "))



        total = calc_coins(quarters ,dimes ,nickles ,pennies )


        if total > cofee_price :

            print(f"\n you gave us : {total} \n")

            change , remaining_resorces = calc_cofee(remaining_resorces , order_details ,total , cofee_price , order)

            print ( f" Here take the change {round(change, 2 )}$  Enjoy your {order} !!!\n")

        elif total == cofee_price :

            print(total)

            change , remaining_resorces = calc_cofee(remaining_resorces , order_details ,total , cofee_price , order)

            print ( f" NO change.  Enjoy your {order} !!! \n")

        elif total < cofee_price :
            print(total)
            print ( f" Not enough Money \n")

        condition = input("Do you want another coffee  type 'y' or 'n'  too check reamainings type 'r' : ")

    else :
        print(" sorry  not enough resorces !")







