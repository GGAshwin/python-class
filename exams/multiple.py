class parent1:
    def abilities(self):
        x=[1,2,3,4]
        return print(x)

class parent2:
    def skills(self):
        y=[7,8,9,10]
        return print(y)

class child(parent1,parent2):
    pass

c=child()
c.skills()
c.abilities()