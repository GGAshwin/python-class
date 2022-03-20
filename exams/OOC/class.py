class point:
    x=10
class another(point):
    def __str__(self):
        return self.x,self.y,self.p.poke

blank=point()
blank.x
blank.y=20
blank.p=another()
blank.p.poke=69

print(blank.p.poke)