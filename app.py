import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()

root.title("PSB-Inventory-Management")

title = tk.Label(root, text="Login", font=("Helvetica", 16))
title.pack()

usernameLabel = tk.Label(root, text="Username")
usernameText = tk.Entry(root, width=20)
usernameLabel.pack()
usernameText.pack()

passwordLabel = tk.Label(root, text="Password")
passwordText = tk.Entry(root, width=20)
passwordLabel.pack()
passwordText.pack()


def addItem():
    res = tk.messagebox.askquestion(
        "Add Item", "Are you sure you want to add this item?")
    print(usernameText.get())


canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

submitBtn = tk.Button(root, text="Submit", command=addItem)
submitBtn.pack()

root.mainloop()
