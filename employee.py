from tkinter import *
from tkinter import messagebox

import mysql.connector


class Emplloyee:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management")
        self.master.geometry("1350x700+0+0")
        self.frame = Frame(master)
        self.frame.pack()

        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.empLabel = Label(self.frame, text="Employee_no")
        self.empLabel.grid(row=1, column=0)

        self.dateLabel = Label(self.frame, text="Date")
        self.dateLabel.grid(row=2, column=0)

        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)

        self.emp_no = Entry(self.frame)
        self.emp_no.grid(row=1, column=1)

        self.date = Entry(self.frame)
        self.date.grid(row=2, column=1)

        def addEmplloyee():
            if self.name.get() == "":
                messagebox.showerror("Error", "Please enter name")
            elif self.emp_no.get() == "":
                messagebox.showerror("Error", "Please enter employee no")
            elif self.date.get() == "":
                messagebox.showerror("Error", "Please enter registerd date")
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
                    cur.execute("insert into employees (name, employee_no, registered_at) values(%s,%s,%s)",
                                (self.name.get(), self.emp_no.get(), self.date.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added")
                except Exception as e:
                    con.rollback()
                    messagebox.showerror("Error", e)

                    con.close()

        self.loginButton = Button(
            self.frame, text="Add Emplloyee", command=addEmplloyee)
        self.loginButton.grid(row=3, column=1)

        total_rows = 5
        total_columns = 4
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.enter = Entry(master, width=20, fg='blue',
                                   font=('Arial', 16, 'bold'))

                self.enter.grid(row=6, column=7)
                self.enter.insert(END, lst[i][j])

        # take the data
        lst = [(1, 'Raj', 'Mumbai', 19),
               (2, 'Aaryan', 'Pune', 18),
               (3, 'Vaishnavi', 'Mumbai', 20),
               (4, 'Rachna', 'Mumbai', 21),
               (5, 'Shubham', 'Delhi', 21)]

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])


master = Tk()
obj = Emplloyee(master)
master.mainloop()
