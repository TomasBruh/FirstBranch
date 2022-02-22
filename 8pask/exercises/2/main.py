
with open("data.txt", "a") as data:
    data.write(" completed")
    data.close()

with open("data.txt", "r") as data:
    print(data.read())
