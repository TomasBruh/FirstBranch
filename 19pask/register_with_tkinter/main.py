from tkinter import *
from user import User

window = Tk()
window.title("Demo")
window.minsize(width=500, height=500)
window_widgets = []
window_entries = []


def has_an_account():
    for widget in window_widgets:
        widget.destroy()
    for entry in window_entries:
        entry.destroy()

    def insert_button_click():
        for item in window_widgets:
            if item.widgetName == "Wrong password":
                item.destroy()
        with open("user_data/data.txt", "r") as r_stream:
            lines = r_stream.readlines()
            r_stream.close()
        users = []
        for line in lines:
            user_info = line.split(" ")
            for i in range(len(user_info)):
                user_info[i] = user_info[i].replace("\n", "")
            users.append(User(user_info[0], user_info[1], user_info[2]))
        given_user = User(input_name.get(), email_input.get(), password_input.get())
        for user in users:
            if user.name == given_user.name and user.email == given_user.email:
                if user.password == given_user.password:
                    succeeded_label = Label(text="You have logged in!")
                    succeeded_label.pack()
                    window_widgets.append(succeeded_label)
                    return
                else:
                    wrong_password_label = Label(text="Wrong password")
                    wrong_password_label.widgetName = "Wrong password"
                    wrong_password_label.pack()
                    window_widgets.append(wrong_password_label)
                    return
        no_user_label = Label(text="Sorry, there is no such user with that name and email in our database")
        no_user_label.pack()
        window_widgets.append(no_user_label)


    name_label = Label(text="Insert your name:")
    name_label.pack()
    window_widgets.append(name_label)

    input_name = Entry(width=30)
    input_name.pack()
    window_entries.append(input_name)

    email_label = Label(text="Insert your email:")
    email_label.pack()
    window_widgets.append(email_label)

    email_input = Entry(width=30)
    email_input.pack()
    window_entries.append(email_input)

    password_label = Label(text="Insert your password:")
    password_label.pack()
    window_widgets.append(password_label)

    password_input = Entry(width=30)
    password_input.pack()
    window_entries.append(password_input)

    insert_button = Button(text="Input", command=insert_button_click)
    insert_button.pack()
    window_widgets.append(insert_button)

    do_not_have_account_button = Button(text="I don't have an account", command=does_not_have_an_account)
    do_not_have_account_button.pack()
    window_widgets.append(do_not_have_account_button)


def does_not_have_an_account():
    for widget in window_widgets:
        widget.destroy()
    for entry in window_entries:
        entry.destroy()

    def insert_button_click():
        with open("user_data/data.txt", "r") as r_stream:
            lines = r_stream.readlines()
            r_stream.close()
        users = []
        for line in lines:
            user_info = line.split(" ")
            users.append(User(user_info[0], user_info[1], user_info[2]))
        given_user = User(input_name.get(), email_input.get(), password_input.get())
        for user in users:
            if user.name == given_user.name and user.email == given_user.email:
                already_exists_label = Label(text="This user already exists")
                already_exists_label.pack()
                return
        with open("user_data/data.txt", "a") as a_stream:
            a_stream.write(f"\n{given_user.name} {given_user.email} {given_user.password}")

    # login

    name_label = Label(text="Insert your name:")
    name_label.pack()
    window_widgets.append(name_label)

    input_name = Entry(width=30)
    input_name.pack()
    window_entries.append(input_name)

    email_label = Label(text="Insert your email:")
    email_label.pack()
    window_widgets.append(email_label)

    email_input = Entry(width=30)
    email_input.pack()
    window_entries.append(email_input)

    password_label = Label(text="Insert your password:")
    password_label.pack()
    window_widgets.append(password_label)

    password_input = Entry(width=30)
    password_input.pack()
    window_entries.append(password_input)

    insert_button = Button(text="Input", command=insert_button_click)
    insert_button.pack()
    window_widgets.append(insert_button)

    have_account_button = Button(text="I have an account", command=has_an_account)
    have_account_button.pack()
    window_widgets.append(have_account_button)


question_label = Label(text="Do you have an account?")
question_label.pack()

insert_answer_yes = Button(text="Yes", command=has_an_account)
insert_answer_no = Button(text="No", command=does_not_have_an_account)
insert_answer_yes.pack()
insert_answer_no.pack()
window_widgets.append(insert_answer_no)
window_widgets.append(insert_answer_yes)
window_widgets.append(question_label)

window.mainloop()
