import mysql.connector


class Connection:
    def __init__(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="ims",
                auth_plugin='mysql_native_password'
            )
            self.conn = con
            print('connet')
        except Exception as e:
            print(e)
