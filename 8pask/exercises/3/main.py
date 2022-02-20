list = []
with open("data.txt", "r") as data:
    list.append(data.readlines())

print(list)
