import re
regex=re.compile(r'from.*\d{1,2}\s([0-9][0-9]):')
text='from lalsjdlkajsdklsat jan 5 09:14:16 2008'
numbebr=regex.findall(text)
print(numbebr)