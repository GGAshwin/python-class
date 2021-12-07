#copy the contents of one file to another
import os
os.chdir('./new_folder')
file1=open('./sample.txt','r')
file2=open('./dest.txt','w')
for i in file1.read():
    file2.write(i)
file1.close()
file2.close()
file=open('./dest.txt','r')
print(file.read())
#completed