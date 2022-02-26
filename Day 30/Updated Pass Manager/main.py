from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Calibri", 12, "bold")

# -------------------------------- SEARCH PASSWORD ----------------------------------- #


def searching():
    website = website_entry.get()
    try:
        with open("Python/#100DaysOfCode/Day 30/Updated Pass Manager/data.json", "r") as file:
            # Reading the Old Data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message= "No Data File Found")
    else:
        if website in data:
            email = data[website]["E-mail"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email/Username: { email } \nPassword: { password }")
        else:
            messagebox.showerror(title= "Error", message= f"No Data on {website}!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    pass_entry.delete(0, END)
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    website = website_entry.get()
    username = uname_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "E-mail": username,
            "Password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Don't leave any fields empty")
    else:
        try:
            with open("Python/#100DaysOfCode/Day 30/Updated Pass Manager/data.json", "r") as file:
                # Reading the Old Data
                data = json.load(file)
        except:
            with open("Python/#100DaysOfCode/Day 30/Updated Pass Manager/data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating the old Data with New data
            data.update(new_data)

            with open("Python/#100DaysOfCode/Day 30/Updated Pass Manager/data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title('Password Manager')
root.config(padx=50, pady=100)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(
    file="Python/#100DaysOfCode/Day 30/Updated Pass Manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_lbl = Label(root, text="Website:", font=FONT)
website_lbl.grid(column=0, row=1)
uname_lbl = Label(root, text="Email/Username:", font=FONT)
uname_lbl.grid(column=0, row=2)
pass_lbl = Label(root, text="Password:", font=FONT)
pass_lbl.grid(column=0, row=3)

# Entry Boxes
website_entry = Entry(root, width=21)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()
uname_entry = Entry(root, width=35)
uname_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
uname_entry.insert(0, "animagus@gmail.com")
pass_entry = Entry(root, width=21)
pass_entry.grid(column=1, row=3, sticky="ew")

# Buttons
gen_pass_btn = Button(root, text="Generate Password",
                      font=FONT, command=generator)
gen_pass_btn.grid(column=2, row=3, sticky="ew")
add_btn = Button(root, text="Add", width=35, font=FONT, command=add_pass)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")
search_btn = Button(root, text="Search", font=FONT, command=searching)
search_btn.grid(column=2, row=1, sticky="ew")
root.mainloop()
