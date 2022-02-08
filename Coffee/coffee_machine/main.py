from menu import Menu
from menu import MenuItem
menu = Menu()
menu.add_menu_item(MenuItem("latte", 0.75, 100, 30, 20))
menu.add_menu_item(MenuItem("cappuccino", 0.50, 60, 20, 10))
menu.add_menu_item(MenuItem("espresso", 0.25, 20, 10, 10))
running = True
while running:
    command = input(f"What would you like? (latte / expresso / cappuccino) ")
    if command == "off":
        running = False
        break
    #for i in range(len(menu)):


