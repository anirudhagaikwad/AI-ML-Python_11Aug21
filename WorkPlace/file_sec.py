f = open("desktop/id.jpg","rb")
for i in f:
    print(i)


f = open("desktop/id.jpg","rb")
f1 =open("desktop/id2.jpg","wb")
bytes = f.read()  
f1.write(bytes)  


f = open("desktop/id.jpg","rb")
f1 =open("desktop/id3.jpg","wb")
for i in f:
    f1.write(i)


#write data to csv file

import csv
with open ("desktop/emp.csv","w",newline="")as f:
    w = csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n = int(input("enter Number of Employee:"))
    for i in range(n):
        eno = input("enter Employee no")
        ename = input("enter Employee name")
        esal = input("enter Employee salary")
        eaddr = input("enter Employee address")
        w.writerow([eno,ename,esal,eaddr])
print("data written successfully") 


#read csv data

import csv
f = open("desktop/emp.csv","r")
r = csv.reader(f)
data = list(r)
# print(data)
for line in data:
    for word in line:
        print(word,"\t",end="")
    print()


#zip

from zipfile import *
f = ZipFile("desktop/All_files1.zip","w",ZIP_DEFLATED)
f.write("desktop/pqr.txt")
f.write("desktop/xyz.txt")
f.write("desktop/xyz1.txt")
f.close()
print("zip file created successfully")


#@@@
from zipfile import *
f = ZipFile("desktop/All_files1.zip","r",ZIP_STORED)
names = f.namelist()
# print(names)
for name in names:
    print("file name:",name)
    print("the content of file is:")
    f1 = open(name,"r")
    print(f1.read())
    print()



    



