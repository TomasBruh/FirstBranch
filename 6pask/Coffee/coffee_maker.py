# class CoffeeMaker
# viskas kas susije su kava, reportu ir resursu
# skaiciavimu
from menu import MenuItem
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resources_sufficient(self, drink):
        can_make = True

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

    def make_coffee(self, order: MenuItem):
        """ Deduct required ingredients from the resources """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"Here is your {order.name}☕. Enjoy!")

    def refill_resources(self):
        """ Refills certain resources """
        water = input("How much water would you like to refill?: ")
        if not type(water) == int:
            print("Amount is only accepted in numbers.")
            return
        milk = input("How much milk would you like to refill?: ")
        if not type(milk) == int:
            print("Amount is only accepted in numbers.")
            return
        coffee = input("How much coffee would you like to refill?: ")
        if not type(coffee) == int:
            print("Amount is only accepted in numbers.")
            return

        resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

        # for resource in resources:
        #     if not type(resource) == int:
        #         print("Amount must be in numbers")
        #         return

        for resource in self.resources:
            self.resources[resource] = resources[resource] + self.resources[resource]
