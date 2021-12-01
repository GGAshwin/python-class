import re
emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
\.[a-zA-Z]{2,5}
)''',re.VERBOSE)
text='ashwinprabhu2001@gmail.com abc@gmail.com  @@@@@.com xyz@lkjldkfjg.com ashwin@jsgf.co.in'
find=emailRegex.findall(text)
print(find)