import os
#a=open('./text.txt','r')
#opens the file in read mode
'''print(a.read())
#returns the content
print(a.readlines())
#returns the list of the content seperated by new line \n'''

'''a=open('./text.txt','w')
a.write('Hello world\n')
a=open('./text.txt','r')
print(a.read())
a.close()'''

#import shelve

'''file=shelve.open('./shelveFile')
cats=['a','b','c']
file['cats']=cats
file.close()'''

'''file=shelve.open('./shelveFile')
print(file['cats'])
file.close()'''

'''file=shelve.open('./shelveFile')
print(list(file.keys()),list(file.values()))
file.close()'''

#class

os.chdir('./new_folder')
print(os.getcwd())

#name=input('Enter file name:')
#file=open(name,'w')
'''content=input()
while True:
    if content=='stop':
        break
    file.write(content+'\n')
    content=input()
file.close()'''

'''name=input("Enter the file you want to read")
readFile=open(name,'r')
contents=readFile.readlines()
read=readFile.read()
print(contents)
print(read)'''


'''count=0
name=input('Enter file name to read from:')
file=open(name,'r')
for i in file:
    print(i,end='')
    count+=1
file.close()
print(count)'''

name=input('Enter file to open:')
file=open(name,'a')
content=input('Enter content:')
while content!='stop':
    file.write(content+'\n')
    content=input()
file.close()

file=open(name,'r')
print(file.read())
file.close()