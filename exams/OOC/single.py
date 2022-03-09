class parent():
    def pshow(self):
        print('Method in parent class')

class child(parent):
    def cshow(self):
        print('Method in child class')

c=child()
c.pshow()
c.cshow()