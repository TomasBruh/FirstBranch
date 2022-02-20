array_of_lines = ["idk", "idk as well"]
with open("data2.txt", "w") as data:
    for i in range(len(array_of_lines)):
        data.write(array_of_lines[i])
data.close()