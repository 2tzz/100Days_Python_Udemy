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
cofee_price = 0


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


order = input("What kind of cofee do you need ? type (espresso/latte/cappuccino) : ")

order_details , cofee_price =  cofee_details(order)


print (order_details , cofee_price)




def calc_cofee ():

    remaining_resorces = {}












