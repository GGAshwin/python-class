import re
regex=re.compile(r'\d{3}\.\d{3}\.\d\.\d+')
ip='192.168.4.1654'
print(regex.findall(ip))