from tkinter import *

window = Tk()
window.title = "Pomodoro"
window.minsize(500, 500)

current_phase = "work"
tomato_count = 0
current_phase_label = Label(text=current_phase)
current_phase_label.grid(row=1, column=0)


def next_phase():
    global current_phase
    global tomato_count
    if tomato_count == 4:
        current_phase = "long break"
        tomato_count = 0
        countdown(25)
    elif current_phase == "work":
        current_phase = "break"
        countdown(5)
    elif current_phase == "break":
        current_phase = "work"
        tomato_count = tomato_count + 1
        countdown(25)
    elif current_phase == "long break":
        current_phase = "work"
        countdown(25)
    current_phase_label.config(text=current_phase)


img = PhotoImage(file="pomodoro_img.png")

pomodoro_img_label = Label(image=img)
pomodoro_img_label.grid(column=0, row=0)

title_label = Label(text="The Pomodoro technique", font=("Times New Roman", 25))
button = Button(text="Start the phase", command=next_phase)
button.grid(column=0, row=2)
title_label.grid(column=1, row=0)


def countdown(count):
    current_phase_label.config(text=count)
    if count > 0 or count == 0:
        window.after(1000, countdown, count-1)


countdown(25)
window.mainloop()
