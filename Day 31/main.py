from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("Python/#100DaysOfCode/Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("Python/#100DaysOfCode/Day 31/data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

root = Tk()
root.title('Flash Card App')
root.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

current_card = {}


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn)
    data.to_csv("Python/#100DaysOfCode/Day 31/data/words_to_learn.csv", index=False)
    new_word()


def new_word():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=fc_front)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(bg_img, image=fc_back)


flip_timer = root.after(3000, func=flip_card)

# Importing all the images
fc_front = PhotoImage(file="Python/#100DaysOfCode/Day 31/images/card_front.png")
fc_back = PhotoImage(file="Python/#100DaysOfCode/Day 31/images/card_back.png")
right_btn = PhotoImage(file="Python/#100DaysOfCode/Day 31/images/right.png")
wrong_btn = PhotoImage(file="Python/#100DaysOfCode/Day 31/images/wrong.png")

# Canvas for the Flashcard window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = canvas.create_image(400, 263, image=fc_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
right = Button(root, image=right_btn, highlightthickness=0, bd=0, command=is_known)
right.grid(column=1, row=1)
wrong = Button(root, image=wrong_btn, highlightthickness=0, bd=0, command=new_word)
wrong.grid(column=0, row=1)

new_word()

root.mainloop()
