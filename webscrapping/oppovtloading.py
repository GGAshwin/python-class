

class A: 
    def __init__(self,a):  #ob1.a = 10
        self.a = a
    def __mul__(self,other):
        return self.a * other.a
obj1= A(10)
obj2 =A(20)
print(obj1 * obj2)
    