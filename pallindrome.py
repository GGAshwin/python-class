string=input('Enter a string:')
x=list(string)
print(x)
list1=x.sort(reverse=True)
list2=""
list2.join(list1)
print(list2==string)