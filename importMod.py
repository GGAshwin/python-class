import pprint
import os
names=[{'name':'abhay','age':100},{'name':'kini','age':10},{'name':'adi','age':1000}]
os.chdir('./new_folder')
file=open('names.py','w')
file.write('name='+pprint.pformat(names)+'\n')
file.close()