#count no.of lines in a file
import os
os.chdir('./new_folder')
file=open('./sample.txt')
print(len(file.readlines()))
#completed