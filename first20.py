#extract the first 20 characeter from a text file
import os
os.chdir('./new_folder')
file=open('./sample.txt','r')
array=(file.read())
n=len(array)
array.strip('\n')
print(array[0:20])
#completed