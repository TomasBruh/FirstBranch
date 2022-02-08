# class MoneyMachine
# Viskas kas susije su pinigais ir paymentu


class Wallet:
    def __init__(self, quarters, dimes, nickles, pennies):
        self.quarters = quarters
        self.dimes = dimes
        self.nickles = nickles
        self.pennies = pennies
        self.amount = self.quarters * 0.25 + self.nickles * 0.05 + self.pennies * 0.01 + self.dimes * 0.10

    def subtract_money(self, quarters, dimes, nickles, pennies):
        if self.amount >= quarters * 0.25 + nickles * 0.05 + pennies * 0.01 + dimes * 0.10:
            if quarters <= self.quarters:
                if dimes <= self.dimes:
                    if nickles <= self.nickles:
                        if pennies <= self.pennies:
                            self.quarters -= quarters
                            self.dimes -= dimes
                            self.nickles -= nickles
                            self.pennies -= pennies
                            return
                        else:
                            print("You do not have enough pennies to buy this coffee")
                    else:
                        print("You do not have enough nickles to buy this coffee")
                else:
                    print("You do not have enough dimes to buy this coffee")
            else:
                print("You do not have enough quarters to buy this coffee")
        else:
            print("You do not have enough money to buy this coffee")
