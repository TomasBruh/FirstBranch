from tkinter import *
from title import Title

window = Tk()
window.title("Demo")
window.minsize(width=50, height=400)
# window.grid_columnconfigure(0, weight=1)
# window.grid_columnconfigure(1, weight=0)

titles = []

with open("data.txt", 'r') as r_stream:
    data_lines = r_stream.readlines()
    r_stream.close()
for data_item in data_lines:
    data_item_split = data_item.split("_-_")
    titles.append(Title(data_item_split[0], data_item_split[1]))

entry_title = Entry(width=50)
entry_title.grid(column=0, row=0, rowspan=2)

replace_button = Button(text="REPLACE")
replace_button.grid(column=1, row=1)

add_button = Button(text="ADD")
add_button.grid(column=0, row=1)


window.mainloop()
