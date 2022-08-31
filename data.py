from sqlite3 import Cursor
import mysql.connector as c

con = c.connect(host="localhost",
                user= "root",
                passwd= "P@$$ward1",
                database= "tufail")

Cursor = con.cursor()
while True:
    IDs = int(input("Enter your ID: "))
    Fname = input("Enter your name: ")
    Desig = input("Enter your designation: ")
    Salary = int(input("Enter your salary: "))
    query = "insert into Tufail_Mobile values ({},'{}','{}',{})".format(IDs, Fname, Desig, Salary)
    Cursor.execute(query)
    con.commit()
    print("Data Inserted....!")