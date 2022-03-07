# def min(s):
#     min = s[0]
#     for i in s:
#         if i < min:
#             min = i
#     return min

# string=input()
# print(min(string))

def min(s):
    mini=s[0]
    for i in range(len(s)-1):
        if(mini>s[i]):
            mini=s[i]
    return mini

string=input()
print(min(string))