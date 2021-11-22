#read multi line input and display the email addresses present
x='''hello
abc@gmail.com
kini@mail.com
skdhf@lkdkjfj.cop
world'''
l=[]
l=x.split('\n')
#print(l)
for i in l:
    if i.endswith('.com'):
        print(i)
    