import re
regex=re.compile(r'^(x\S:)(\d+)$')

obj=regex.search('x$:7894').group(2)
x=list(str(obj))
for i in range(len(x)):
    x[i]=int(x[i])
print(sum(x))
