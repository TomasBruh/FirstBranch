from prettytable import PrettyTable
import random
x = PrettyTable()

x.field_names = ["City", "Area", "Population"]
x.add_row(["Adelaide", 1295, 1158259])
x.add_row(["Brisbane", 1295, 1158259])
x.add_row(["Darwin", 1295, 1158259])
x.add_row(["Hobart", 1295, 1158259])
x.add_row(["Sydney", 1295, 1158259])

print(x)

german_cars = ["BMW", "Audi", "MB", "Porsche"]
print(random.randint(0, 100))
print(random.randrange(10, 100, 5))  # 10, 15, 20, 25... 95, 100.

print(random.choice(german_cars))
random.shuffle(german_cars)
print(german_cars)
german_cars.sort()
print(german_cars)
