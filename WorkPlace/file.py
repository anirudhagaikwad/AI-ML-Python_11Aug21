f = open('desktop/xyz1.txt','w')
print('name:',f.name)
print('mode:',f.mode)
print('closed:',f.closed)
print('is readable:',f.readable())
print('is writable:',f.writable())
f.close()
print('closed:',f.closed)

#write data

f = open('desktop/xyz.txt','w')
f.write('java\n')
f.write('programming\n')
f.write('lang\n')
print('write data sucessfully')
f.close()

#write list

f = open('desktop/xyz.txt','w')
list = ['c\n','c++\n','java\n','pyhton\n','sql\n','data science\n']
f.writelines(list)
print("list of lines write sucessfully")
f.close()

#read total data
f = open('desktop/xyz.txt','r')
data = f.read()
print(data)
f.close()


#first 10 char 


f = open('desktop/xyz.txt','r')
data = f.read(10)
print(data)
f.close()

#read line by line

f = open('desktop/xyz.txt','r')
line1 = f.readline()
print(line1,end="")
line2 = f.readline()
print(line2,end="")
line3 = f.readline()
print(line3,end="")
line4 = f.readline()
print(line4,end="")
f.close()


#read all lines into list


f = open('desktop/xyz.txt','r')
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()    




