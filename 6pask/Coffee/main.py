from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What you would like? ({options}) ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill_resources()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payments(drink.cost):
                coffee_maker.make_coffee(drink)
