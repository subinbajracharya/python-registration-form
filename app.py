import tkinter as tk
from tkinter import StringVar, Entry, IntVar

from lib2to3.fixer_util import String
from tkinter.ttk import Label

root = tk.Tk()  # Create a main window
root.geometry("500x300")
Label(root, text="Python Registration Form", font="Arial 18 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
payment_mode = Label(root, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
payment_mode.grid(row=4, column=2)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
payment_mode_value = StringVar()
check_value = IntVar

name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_mode_entry = Entry(root, textvariable=payment_mode_value)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
payment_mode_entry.grid(row=4, column=3)

root.mainloop()  # Start the Tkinter event loop
