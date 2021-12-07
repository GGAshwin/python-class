#extract last 20 characters from a file
import os
os.chdir('./new_folder')
file=open('./sample.txt','r')
array=(file.read())
n=len(array)
array.strip('\n')
print(array[-21:])
#completed