german_cars = ["bmw", "audi", "mb", "porsche", "vw"]
my_mustang = {
    "brand": "Ford:",
    "model": "Mustang:",
    "year": 1969,
    "good_condition": True,
}

for car in german_cars:
    print(car)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for car in german_cars[2:4]:
    print(car)

for x in range(5, 100, 5):
    print(x)

for key, value in my_mustang.items():
    print(f"Key: {key}: \t Value: {value}")
