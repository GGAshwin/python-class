import re
regex=re.compile(r'\d{4}\s\d{4}\s\d{4}')
regex2=re.compile(regex)
text='1111 2222 3333 4561 2314 1523 4567 1123 5647'

print(regex2.findall(text))