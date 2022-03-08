import re
regex=re.compile(r'[$#@!]+[a-z]+[A-Z]+')

# def check(s):
#     if(len(s)<6):
#         return False
#     else:
#         obj=regex.search(s).group()
#         return obj

# s='$#@!AzaZ'
# if check(s):
#     print("Password valid",check(s))
# else:
#     print("password invalid")

s='$#@!AzaZ'
obj=regex.findall(s)
print(obj)