from tkinter import *
from tkinter import messagebox

import mysql.connector


class Item:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management")
        self.master.geometry("1350x700+0+0")
        self.frame = Frame(master)
        self.frame.pack()

        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.cateLabel = Label(self.frame, text="Category")
        self.cateLabel.grid(row=1, column=0)

        self.qtyLabel = Label(self.frame, text="Qty")
        self.qtyLabel.grid(row=2, column=0)

        self.priceLabel = Label(self.frame, text="Price")
        self.priceLabel.grid(row=3, column=0)

        self.dateLabel = Label(self.frame, text="Date")
        self.dateLabel.grid(row=4, column=0)

        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)

        self.cate = Entry(self.frame)
        self.cate.grid(row=1, column=1)

        self.qty = Entry(self.frame)
        self.qty.grid(row=2, column=1)

        self.price = Entry(self.frame)
        self.price.grid(row=3, column=1)

        self.date = Entry(self.frame)
        self.date.grid(row=4, column=1)

        def addItem():
            if self.name.get() == "":
                messagebox.showerror("Error", "Please enter name")
            elif self.cate.get() == "":
                messagebox.showerror("Error", "Please enter category")
            elif self.qty.get() == "":
                messagebox.showerror("Error", "Please enter qty")
            elif self.price.get() == "":
                messagebox.showerror("Error", "Please enter price")
            elif self.date.get() == "":
                messagebox.showerror("Error", "Please enter date")
            else:
                try:
                    con = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="12345678",
                        database="ims",
                        auth_plugin='mysql_native_password'
                    )
                    cur = con.cursor()
                    cur.execute("insert into items (name, category, qty, price, date) values(%s,%s,%s,%s,%s)",
                                (self.name.get(), self.cate.get(), self.qty.get(), self.price.get(), self.date.get()))
                    # self.framet.destroy()
                    getItem()
                    con.commit()
                    messagebox.showinfo("Success", "Item added")
                except Exception as e:
                    con.rollback()
                    messagebox.showerror("Error", e)

                    con.close()

        self.loginButton = Button(self.frame, text="Add Item", command=addItem)
        self.loginButton.grid(row=5, column=1)

        self.search = Entry(self.frame)
        self.search.grid(row=6, column=0)

        self.framet = Frame(master)
        self.framet.pack()

        def searchItem():
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="12345678",
                    database="ims",
                    auth_plugin='mysql_native_password'
                )
                cur = con.cursor()
                cur.execute("select * from items where name like %s",
                            (self.search.get(),))

                lst = cur.fetchall()
                # find total number of rows and
                # columns in list
                total_rows = len(lst)
                total_columns = len(lst[0])

                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                        self.table = Entry(self.framet, width=20, fg='blue',
                                           font=('Arial', 16, 'bold'))
                        self.table.grid(row=i, column=j)
                        self.table.insert(END, lst[i][j])

                con.commit()
            except Exception as e:
                con.rollback()
                messagebox.showerror("Error", e)

                con.close()

        self.searchButton = Button(
            self.frame, text="Search", command=searchItem)
        self.searchButton.grid(row=6, column=1)

        def getItem():

            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="12345678",
                    database="ims",
                    auth_plugin='mysql_native_password'
                )
                cur = con.cursor()
                cur.execute("select * from items")

                lst = cur.fetchall()
                # find total number of rows and
                # columns in list
                total_rows = len(lst)
                print(total_rows)
                total_columns = len(lst[0])

                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                        self.table = Entry(self.framet, width=20, fg='blue',
                                           font=('Arial', 16, 'bold'))
                        self.table.grid(row=i, column=j)
                        self.table.insert(END, lst[i][j])

                con.commit()
            except Exception as e:
                con.rollback()
                messagebox.showerror("Error", e)

                con.close()

        getItem()


master = Tk()
obj = Item(master)
master.mainloop()
