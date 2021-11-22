#read multi line input from keyboard and displlay the following 1.no.of.line present 2.no.of.words present 3.no.of.article lines present 
lines=[]
while 1:
    line=input()
    if line:
        lines.append(line)
    else:
        break
print(lines)
x='''Hello
World fan
Apple bottle laptop
Hi
How
Are
You'''
count=1
for i in lines:
    if i=='\n':
        count=count+1
print('No.of.line is '+str(count))
count=0
test=lines.split()
print('Number of words is '+str(len(test)))
count=0
for i in lines:
    if i.istitle()==True:
        count=count+1
print('Number of articles are '+str(count))