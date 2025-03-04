from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menux = Menu()
coffeemaker = CoffeeMaker ()
moneymachine = MoneyMachine ()

menux.__init__()
coffeemaker.__init__()
moneymachine.__init__()




order = input(f"What kind of cofee do you need ? type ({menux.get_items()}) or type (report) to get a report : ")


if order  == 'latte' or order  == 'cappuccino' or order  == 'espresso' :


    if moneymachine.make_payment(menux.find_drink(order).cost) == True :

        coffeemaker.make_coffee(menux.find_drink(order))
    

elif order == 'report':

    coffeemaker.report()
    moneymachine.report()

else :
    print(menux.find_drink(order))

