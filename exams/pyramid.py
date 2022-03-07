n=9
star='*'
c=1
for i in range(1,6):
    print(star.center(n, '-'))
    c+=2
    star='*'*(c)
