import re
agentname =re.compiler(r'''(
(\d{3}|\(\d{3}\))?)
[\s-] 
\d{3}
[\s-] 
\d{4}
)''',re.VERBOSE)

str='dcbddbcd bdbcbsd :(535)-555-7777 andj hjbububugbu '
phone=agentname.findall(str)
print(phone)