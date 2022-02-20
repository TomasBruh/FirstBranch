with open("data.txt", "r") as data:
    array_of_lines = data.readlines()
data.close()
array_of_words = []
text = ""
for i in array_of_lines:
    text = text + i
text = text.replace("\n", " ")
array_of_words = text.split(" ")
longest_word = array_of_words[0]
for i in array_of_words:
    if len(longest_word) < len(i):
        longest_word = i
print(longest_word)