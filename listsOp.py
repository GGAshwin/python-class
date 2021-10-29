
N = int(input())
L = []
for i in range(N):
    a = input().split()
    b = a.pop(0)
    if b == "append":
        L.append(int(a[0]))
    elif b == "insert":
        L.insert(int(a[0]), int(a[1]))
    elif b == "remove":
        L.remove(int(a[0]))
    elif b == "print":
        print(L)
    elif b == "sort":
        L.sort()
    elif b == "pop":
        L.pop()
    elif b == "reverse":
        L.reverse()