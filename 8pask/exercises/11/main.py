with open("data.txt", "r") as data:
    array_of_lines = data.readlines()
data.close()
with open("data2.txt", "w") as data:
    for i in range(len(array_of_lines)):
        data.write(array_of_lines[i])
data.close()