#check again
n = int(input("How many terms? "))
n1, n2 = 0, 1
l=[]
print("Fibonacci sequence:")
for i in range(n):
    l.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
print(l)