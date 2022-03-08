import re
regexName=re.compile(r'[a-zA-Z]+\sNakamoto')
searchobj=regexName.search(input())
print(searchobj.group())