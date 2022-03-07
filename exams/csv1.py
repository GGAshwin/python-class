from asyncore import write
import csv

file=open('file.csv','a',newline='\n')

# read=csv.reader(file)

# data=list(read)
# print(data)

write=csv.writer(file)
write.writerow([3,'ady'])