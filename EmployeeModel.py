
from Conn import Conn


class EmployeeModel(Conn):

    def get(self):
        super()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM employees")
        list = cur.fetchall()
        self.conn.close()
        return list

    def create(self, name, emp_no, date):
        super()
        val = (name, emp_no, date)
        cur = self.conn.cursor()
        cur.execute(
            "insert into employees (name, employee_no, registered_at) values(%s,%s,%s)", val)
        self.conn.commit()
        self.conn.close()
        return True

    def update(self, id, name, emp_no, date):
        super()
        val = (name, emp_no, date, id)
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE employees SET name = %s, emp_no = %s, date = %s WHERE id = %s", val)
        self.conn.commit()
        self.conn.close()
        return True

    def delete(self, id):
        super()
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM employees WHERE id = " +
                        str(id))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def show(self, id):
        super()
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def search(self, name):
        super()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM employees WHERE name LIKE " +
                    "'"+str(name)+"%'")
        list = cur.fetchall()
        self.conn.close()
        return list


# ItemModel().update(5, 'test A', 'test cate A', 67, 68.00, '2020-04-01')
# #ItemModel().create('test', 'test cate', 65, 65.00, '2020-01-01')
# print(ItemModel().get())
