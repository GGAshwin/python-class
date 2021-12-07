import shutil
import os
for folderName,subfolders,filenames in os.walk('/home/ashwin/Desktop/python-class/new_folder'):
    print('The current folder is:'+folderName)
    for subfolder in subfolders:
        print('Subfolder:'+folderName+' '+subfolder)
    for filename in filenames:
        print('filename:'+folderName+' '+filename)
        if(filename=='ashwin'):
            print('Found '+filename)
            break
    print('\n\n')