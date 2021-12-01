import os
'''cwd=os.getcwd()
print(cwd)
print(os.path.join(os.getcwd(),'a','b','c'))'''

'''myfiles=['acc.txt','test.cpp','apple.c']
for i in myfiles:
    print(os.path.join(os.getcwd(),i))
os.chdir('../')
print(os.getcwd())'''

#os.chdir('/home/ashwin/Desktop')
#print(os.getcwd())
#print(os.path.abspath('./python-class'))
#print(os.path.isabs('/home/ashwin/Desktop'))
#print(os.path.relpath('/home/ashwin/Desktop/python-class/adhar.py'))
#print(os.path.dirname('/home/ashwin/Desktop'))

path='/home/ashwin/Desktop/python-class'
'''print(path.split(os.path.sep))
print(os.path.getsize(path))
print(os.listdir(path))'''

'''size=0
for i in os.listdir(path):
    print(i)
    size=size+os.path.getsize(os.path.join(path,i))
print(size)'''

print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))