import os
os.makedirs('./sum')
os.chdir('./sum')
file=open('./new','w')
file.write('Hello world')
file.close()
fileR=open('./new','r')
print(fileR.read())
#completed