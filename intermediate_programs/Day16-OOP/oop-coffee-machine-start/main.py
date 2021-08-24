# Elvin Rivera
# Date Created: 8/1/2021
# Reference: https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
    #     if coffee_maker.is_resource_sufficient(drink):
    #         # .cost comes from the MenuItem class
    #         # There's a function to collect coins in make_payment()
    #         if money_machine.make_payment(drink.cost):
    #             coffee_maker.make_coffee(drink)
    #      # another approach is to turn the two comparisons into variable and check that
        #      e.g. if is_sufficient and is_payment successful:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



