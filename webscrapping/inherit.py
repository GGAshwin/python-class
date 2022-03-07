class A:
    def hello(self):
        print("Hello")
class B(A):
    def world(self):
        print("World")

a = A()
a.world()
b = B()
b.hello()