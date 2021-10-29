num=153
temp=num

d1=temp%10
print(d1)
temp//=10

d2=temp%10
print(d2)
temp=temp//10


d3=temp
print(d3)
temp//10

if(d1**3 + d2**3 + d3**3 ==num):
    print('Armstrong number')