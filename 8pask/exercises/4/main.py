text = ""
with open("data.txt", "r") as data:
    temp = data.readlines()

data.close()
for i in temp:
    text = text + i
print(text)
