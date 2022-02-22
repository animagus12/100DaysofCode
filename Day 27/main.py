from cProfile import label
from tkinter import Tk

from tkinter import *
from PIL import ImageTk, Image
from matplotlib.pyplot import text

root = Tk()
root.title('')
root.geometry('400x400')

my_label = Label(root, text="Im a Label", font = ("Arial", 24, "bold"))
my_label.pack()


root.mainloop()
