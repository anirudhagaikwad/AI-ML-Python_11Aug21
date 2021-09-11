import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "" )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase2")


import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database="mydatabase2" )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(id  INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#@@@

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name,address)VALUES(%s,%s)"
val = [("pramod","Pune"),("Pravin","Solapur"),("Anand","Pune"),("Amar","Solapur"),("Ramesh","Pune"),("Amit","Pune"),("Ashutosh","Mumbai")]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")

#@@@

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'Solapur'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#@@@

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY id desc"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#@@@@@@
import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mumbai'"

mycursor.execute(sql)



#update

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Nashik' WHERE address = 'Solapur'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount,"record affected")

#@@@@

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase2" )
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)














