

from cgi import print_directory


class A: 
    def __init__(self,a,b):
        self.a = a
        self.b= b
    def add(self):
        return self.a + self.b
    def __str__(self):
        return "Done"
obj = A(10,20)
print(obj)

print(obj.add())        