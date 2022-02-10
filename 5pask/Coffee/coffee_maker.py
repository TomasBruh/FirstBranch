# class CoffeeMaker
# viskas kas susije su kava, reportu ir resursu
# skaiciavimu
class CoffeeMaker:
    def __init__(self, milk, water, coffee):
        self.milk = milk
        self.water = water
        self.coffee = coffee

    def make_coffee(self, milk, water, coffee):
        if self.milk >= milk:
            if self.water >= water:
                if self.coffee >= coffee:
                    self.milk -= milk
                    self.water -= water
                    self.coffee -= coffee
                else:
                    print("Sorry, but you we've run out of coffee")
            else:
                print("Sorry, but you we've run out of water")
        else:
            print("Sorry, but you we've run out of milk")
