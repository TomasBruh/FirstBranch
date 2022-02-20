count_of_lines = 0
with open("data.txt", "r") as data:
    array_of_lines = data.readlines()
data.close()
count_of_lines = len(array_of_lines)
print(count_of_lines)
