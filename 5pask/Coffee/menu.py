# class MenuItem vienas gerimas
# class Menu gerimu array, viskas kas susije su menu.

class MenuItem:
    def __init__(self, name, cost, milk, coffee, water):
        self.name = name
        self.cost = cost
        self.milk = milk
        self.coffee = coffee
        self.water = water


class Menu:
    def __init__(self):
        self.list = []

    def add_menu_item(self, menu_item):
        self.list.append(menu_item)
