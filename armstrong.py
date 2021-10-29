#display armstrong numbers from 100 to 1000
for num in range(100,1000):
    sum=0
    temp=num
    while temp>0:
        sum+=(temp%10)**3
        temp//=10
    if num==sum:
        print(num)