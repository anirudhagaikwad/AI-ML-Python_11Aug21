#with statement
with open('desktop/xyz1.txt','w') as f:
    f.write("python\n")
    f.write("java\n")
    f.write("sql")
    print("is file closed:",f.closed)
print("is file closed:",f.closed)


#tell()

f = open('desktop/xyz1.txt','r')
print(f.tell())
print(f.read(3))
print(f.tell())


#seek()

data = "ALL Students are intelligent"
f = open("desktop/xyz.txt","w")
f.write(data)
with open ("desktop/xyz.txt","r+") as f:
    text = f.read()
    print(text)
    print("the current cursor position",f.tell())
    f.seek(17)
    print("the current cursor position",f.tell())
    f.write("bright")
    f.seek(0)
    text = f.read()
    print(text)


#Flie exit or not 

import os,sys
fname = input("Enter file name:")
if os.path.isfile(fname):
    print("File Exists:",fname)
    f = open(fname,'r')
else:
    print("File doesnot exists:",fname) 
print("the content of file is:")
data=f.read()
print(data) 




