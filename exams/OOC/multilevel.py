class ancestor:
    def ashow(self):
        print('ancestor show')

class parent(ancestor):
    def pshow(self):
        print('Parent show')

class child(parent):
    def __init__(self,name):
        self.name=name
c=child('boy')
c.pshow()
c.ashow()

p=parent()
p.ashow()
