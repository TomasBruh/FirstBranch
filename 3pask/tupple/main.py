my_tuple = ("lol", "lmao ")
# su paprastais skliaustais, read_only

print(my_tuple[1])
print(my_tuple[0: 1])
print(my_tuple[1:])
print(my_tuple[1])

x = list(my_tuple)
x.append("Dell")

print(my_tuple)

colors = (255, 207, 102)
(red, green, blue) = colors

print(f"Red: {red}, Green: {green}, Blue: {blue}")
