
# class MoneyMachine
# Viskas kas susije su pinigais ir paymentu


class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """ Return total calculated from coins inserted """
        money_received = 0
        print("Please insert the coins:")
        for coin in self.COIN_VALUES:
            money_received += int(input(f"How many {coin}")) * self.COIN_VALUES[coin]
        return money_received

    def make_payments(self, cost):
        """ Return True when payment is accepted or False when it is not """
        money_received = self.process_coins()

        if money_received >= cost:
            change = round(money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print(f"Sorry, that's not enough money ({self.CURRENCY}{money_received} refunded)")
            return False
