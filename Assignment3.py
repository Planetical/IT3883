# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab3
# Due Date: 10/3/2025
# Purpose: Create a GUI that converts miles per gallon to kilometers per liter

import tkinter as tk


# function to convert miles per gallon to kilometers per liter
def convert_mpg(*_):
    mpg_value = mpg_var.get()
    try:
        kml_var.set(float(mpg_value) * 0.425143707)
    except ValueError:  # if letter is input...
        kml_var.set(0.0)


# creating GUI
root = tk.Tk()
root.title("MPG to km/l")
root.geometry("300x200")

# saving mpg and km/l as variables in tk to be updated later
mpg_var = tk.StringVar()
kml_var = tk.DoubleVar()

# watching for write
mpg_var.trace_add("write", convert_mpg)

# mpg block with padding at the bottom
mpg = tk.Entry(root, textvariable=mpg_var)
mpg.pack()
mpg_label = tk.Label(root, text="mpg")
mpg_label.pack(pady=(0, 40))

# kml block
kml = tk.Label(root, textvariable=kml_var)
kml.pack()
kml_label = tk.Label(root, text="km/L")
kml_label.pack()

root.mainloop()
