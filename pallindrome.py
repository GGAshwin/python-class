str=input('Enter a str:')
l=str.split()
a=l.sort(reverse=True)
print(a)
str1=''.join(l)
print(l)
if str==str1:
    print('pallindrome')
else:
    print('no')