# class MoneyMachine
# Viskas kas susije su pinigais ir paymentu


class MoneyMachine:
    def __init__(self, money=0):
        self.money = money

    def make_a_payment(self, quarters, dimes, nickles, pennies, cost):
        amount = quarters * 25 + dimes * 10 + nickles * 5 + pennies * 1
        if amount >= cost:
            amount -= cost
        self.money += cost
        return amount / 100
