import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1', database='ims', auth_plugin='mysql_native_password')

mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM admins")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

cnx.close()
