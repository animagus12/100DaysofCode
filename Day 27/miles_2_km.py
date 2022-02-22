from tkinter import *

root = Tk()
root.title('Mile to Km Converter')
# root.geometry('400x400')
root.config(padx=30, pady=30)


def calculoator():
    miles = int(entry.get())
    print(miles)
    km = miles * 1.60934
    print(km)
    label_4 = Label(root, text=km)
    label_4.grid(column=1, row=1)


entry = Entry(root, width=15)
entry.grid(column=1, row=0)
entry.insert(0, "")


label_1 = Label(root, text="is equal to ")
label_1.grid(column=0, row=1)

label_2 = Label(root, text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(root, text="Km")
label_3.grid(column=2, row=1)

btn = Button(root, text="Calculate", command=calculoator)
btn.grid(column=1, row=2)

root.mainloop()
