
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

from matplotlib.pyplot import text, title
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    root.after_cancel(timer)
    title_lbl.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    count_lbls.config(text= "")
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        title_lbl.config(text="Break", fg=RED)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        title_lbl.config(text="Break", fg=PINK)
    elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        title_lbl.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "🗸"
        count_lbls.config(text= mark)
            

# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title('POMODORO')
# root.geometry('400x400')
root.config(padx=100, pady=50, bg=YELLOW)


title_lbl = Label(root, text="Timer", fg=GREEN, bg=YELLOW, font=FONT)
title_lbl.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file="Python/#100DaysOfCode/Day 28/tomato.png")
canvas.create_image(100, 112, image=logo)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

start_btn = Button(root, text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(root, text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

count_lbls = Label(root, fg=GREEN, bg=YELLOW, font=FONT)
count_lbls.grid(column=1, row=3)

root.mainloop()
