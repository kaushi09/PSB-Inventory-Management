from tkinter import *


class Dashboard:
    def __init__(self, master):

        self.master = master
        self.master.title("PSB-Inventory-Management")
        self.master.geometry("1350x700+0+0")
        self.frame = Frame(master)
        self.frame.pack()

        self.loginButton = Button(
            self.frame, text="Items Store", command=self.showItem)
        self.loginButton.grid(row=5, column=1)

        self.loginButton = Button(
            self.frame, text="Employee List", command=self.showEmployee)
        self.loginButton.grid(row=5, column=2)

    def showItem(self):
        print("Items Store")

    def showEmployee(self):
        print("fafa Store")


# master = Tk()
# obj = Dashboard(master)
# master.mainloop()
