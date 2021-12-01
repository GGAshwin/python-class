
import re
regex=re.compile(r'\S*URL:\S*rev=([0-9]+)\S*')
str='URL:https://www.w3schools.com/python/python_regex.asp#findall/rev=54641,URL:https://www.w3schools.com/python/python_regex.asp#findall/rev=7879787'
something=regex.findall(str)
print(something)