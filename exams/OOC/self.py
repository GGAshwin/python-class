class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __str__(self):
        return "%d,%d"%(self.x,self.y)
p1=point(5,6)
p2=point(1,2)
print("p1 is:",p1)
print("p1 is:",p2)