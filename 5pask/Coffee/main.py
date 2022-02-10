from menu import Menu
from menu import MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
import random

menu = Menu()
menu.add_menu_item(MenuItem("latte", 75, 100, 30, 20))
menu.add_menu_item(MenuItem("cappuccino", 50, 60, 20, 10))
menu.add_menu_item(MenuItem("espresso", 25, 20, 10, 10))

wallet = MoneyMachine()

coffee_maker = CoffeeMaker(
    random.randrange(100, 300, 25),
    random.randrange(150, 350, 25),
    random.randrange(25, 125, 25))

running = True
while running:
    key_word = input(f"What would you like? (latte / expresso / cappuccino): ")
    if key_word == "off":
        running = False
        break
    found_flag = False
    if key_word == "report":
        print(f"Milk: {coffee_maker.milk}ml")
        print(f"Coffee: {coffee_maker.coffee}g")
        print(f"Water: {coffee_maker.water}ml")
        print(f"Money: ${wallet.money}")
        found_flag = True
    for menuItem in menu.list:
        if key_word == menuItem.name:
            if coffee_maker.coffee >= menuItem.coffee:
                if coffee_maker.milk >= menuItem.milk:
                    if coffee_maker.water >= menuItem.water:
                        print("Please insert the coins.")
                        change = wallet.make_a_payment(
                            int(input("Input quarters: ")),
                            int(input("Input dimes: ")),
                            int(input("Input nickles: ")),
                            int(input("Input pennies: ")),
                            menuItem.cost)
                        print(f"Here is your ${change} in change.")
                        print(f"Here is your {menuItem.name} ☕. Enjoy!")

                        coffee_maker.coffee -= menuItem.coffee
                        coffee_maker.milk -= menuItem.milk
                        coffee_maker.water -= menuItem.water

                        found_flag = True
                    else:
                        print("Sorry, there is not enough water.")
                        found_flag = True
                else:
                    print("Sorry, there is not enough milk.")
                    found_flag = True
            else:
                print("Sorry, there is not enough coffee.")
                found_flag = True
    if not found_flag:
        print("Sorry, but there is no such coffee available")
