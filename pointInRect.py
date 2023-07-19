class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x,self.y)
class Rect:
    def __init__(self,p1,p2):
        self.lowerleft = p1
        self.upperright = p2
    def area(self):
        h = self.upperright.y - self.lowerleft.y
        #it saved in Point class then accessing x need to use artribute .x 
        #and self.upperight is an artribute in Rect claas(name of a factor)
        l = self.upperright.x - self.lowerleft.x
        #call form Point class 
        return str(h*l)
    def contains(self,p):
        if (self.upperright.y>= p.y>=self.lowerleft.y )and (self.upperright.x>=p.x>=self.lowerleft.x) :
            return True
        else:
            return False
x1, y1, x2, y2 = [int(e) for e in input().split()]
lowerleft = Point(x1, y1)
upperright = Point(x2, y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
   x, y = [int(e) for e in input().split()]
   p = Point(x, y)
   print(rect.contains(p))
    