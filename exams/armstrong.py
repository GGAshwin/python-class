n=153
sum=0
temp=n

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

print(sum)