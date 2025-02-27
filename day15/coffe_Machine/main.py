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


    else:
        return 0

def calc_coins(quarters ,dimes ,nickles ,pennies ):

        return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

order = input("What kind of cofee do you need ? type (espresso/latte/cappuccino) : ")

order_details , cofee_price =  cofee_details(order)


print(f"{order}  will be {cofee_price}$  plese  enter coins below \n")

quarters = int(input("put quaters  here : "))
dimes = int(input("put dimes  here : "))
nickles = int(input("put nickles  here : "))
pennies = int(input("put pennies  here : "))

total = calc_coins(quarters ,dimes ,nickles ,pennies )


print(total)

print (order_details , cofee_price)


#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

def calc_cofee (resources , input_resorces , input_price  , item_price):

    change = 0

    resources["water"] = resources["water"] - input_resorces["water"]

    change = input_price - item_price

    return change , resources

change , remaining_resorces = calc_cofee(resources , order_details ,total , cofee_price)

print ( change , remaining_resorces)












