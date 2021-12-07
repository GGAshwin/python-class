import os
import shelve


os.chdir('./shelf')
'''file=shelve.open('test')
x='a**2+b**2+2ab'
colors=['red','blu','black']
obj={
    1:'apple',
    2:'ball',
    3:'differential equation'
}
file['x']=x
file['colors']=colors
file['obj']=obj
file.close()'''

file=shelve.open('./Mydata',)

print(list(file.keys()))

print('\n')
for i in range(0,100):
    print('*',end='')
print('\n')

for i in file.keys():
    print(file[i])
print('\n')

for i in range(0,100):
    print('*',end='')
print('\n')

for i in file.values():
    print(i)
file.close()