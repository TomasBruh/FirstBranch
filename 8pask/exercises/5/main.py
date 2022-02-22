
with open("data.txt", "r") as data:
    array_of_lines = data.readlines()
data.close()
array_of_words = []
text = ""
for i in array_of_lines:
    text = text + i
text = text.replace("\n", " ")
array_of_words = text.split(" ")
print(array_of_words)
