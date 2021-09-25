from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from EmployeeModel import EmployeeModel


class Employee:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management - Employee")
        self.master.geometry("1350x700+0+0")
        self.frame = Frame(master)
        self.frame.pack()

        # Form-----------------------------------------------------
        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.empLabel = Label(self.frame, text="Employee_no")
        self.empLabel.grid(row=1, column=0)

        self.dateLabel = Label(self.frame, text="Registered at")
        self.dateLabel.grid(row=2, column=0)

        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)

        self.emp_no = Entry(self.frame)
        self.emp_no.grid(row=1, column=1)

        self.date = Entry(self.frame)
        self.date.grid(row=2, column=1)

        self.loginButton = Button(
            self.frame, text="Add Employee", command=self.addEmployee)
        self.loginButton.grid(row=3, column=1)

        self.showButton = Button(
            self.frame, text="Recieved Items", command=self.showItem)
        self.showButton.grid(row=3, column=2)

        self.assignButton = Button(
            self.frame, text="Assign Items", command=self.assignItem)
        self.assignButton.grid(row=3, column=3)

        # Sort---------------------------
        self.col = Combobox(self.frame, values=(
            'name', 'employee_no', 'registered_at'))
        self.col.grid(row=6, column=1)

        self.order = Combobox(self.frame, values=('asc', 'desc'))
        self.order.grid(row=6, column=2)

        self.searchButton = Button(
            self.frame, text="Sort", command=self.sortItem)
        self.searchButton.grid(row=6, column=3)

        # Search---------------------------
        self.search = Entry(self.frame)
        self.search.grid(row=6, column=4)

        self.searchButton = Button(
            self.frame, text="Search", command=self.searchItem)
        self.searchButton.grid(row=6, column=5)

        # Table-----------------------------------------------------
        self.getEmployee()

    def addEmployee(self):
        if self.name.get() == "":
            messagebox.showerror("Error", "Please enter name")
        elif self.emp_no.get() == "":
            messagebox.showerror("Error", "Please enter employee no")
        elif self.date.get() == "":
            messagebox.showerror("Error", "Please enter registerd date")
        else:
            try:
                EmployeeModel().create(self.name.get(), self.emp_no.get(), self.date.get())
                self.framet.destroy()
                self.getEmployee()
                messagebox.showinfo("Success", "Employee added")
            except Exception as e:
                messagebox.showerror("Error", e)

    def getEmployee(self):
        self.framet = Frame(self.master)
        self.framet.pack()

        try:

            lst = EmployeeModel().get()
            # find total number of rows and
            # columns in list
            total_rows = len(lst)
            total_columns = len(lst[0])

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.table = Entry(self.framet, width=20,
                                       font=('Arial', 16, 'bold'))
                    self.table.grid(row=i, column=j)
                    self.table.insert(END, lst[i][j])
        except Exception as e:
            messagebox.showerror("Error", e)

    def showItem(self):
        self.frame.destroy()
        self.framet.destroy()

    def assignItem(self):
        self.frame.destroy()
        self.framet.destroy()

    def sortItem(self):
        self.frame.destroy()
        self.framet.destroy()

    def searchItem(self):
        self.frame.destroy()
        self.framet.destroy()

    def clearFrame(self):
        self.frame.destroy()
        self.framet.destroy()


master = Tk()
obj = Employee(master)
master.mainloop()
