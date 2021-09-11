import mysql.connector

myconn = mysql.connector.connect(host= "localhost", user = "root",password = "" )
print("\n database connection established:",myconn)
cur = myconn.cursor()
print("curser:",cur)


# create database
import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "" )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase1")



#create table
import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase1" )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(50),address VARCHAR(100))")

#show database and table
import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase1" )
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
      print(x)




#insert values into table


import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase1" )
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name,address)VALUES(%s,%s)"
val = ("Anand","solapur")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")


#multiple insert values

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase1" )
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name,address)VALUES(%s,%s)"
val = [("Pramod","pune"),("Amar","Solapur"),("Avinash","pune")]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")


#fetch data

import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = "root",password = "",database = "mydatabase1" )
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
for x in myresult:
      print(x)








