from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menux = Menu()

menux.__init__()

order = input(f"What kind of cofee do you need ? type ({menux.get_items()}) : ")

print(order)

if order  == 'latte' or order  == 'cappuccino' or order  == 'espresso' :
    water_amount = menux.find_drink(order).ingredients["water"]
    coffee_amount = menux.find_drink(order).ingredients["coffee"]
    milk_amount = menux.find_drink(order).ingredients["milk"]
    order_cost = menux.find_drink(order).cost
    print(water_amount , coffee_amount , milk_amount)

else :
    print(menux.find_drink(order))

