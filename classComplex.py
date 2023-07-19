class Complex:
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def __str__(self):
        if self.a ==0:
            if self.b<0 and self.b!=-1:
                return str(self.b)+"i"
            elif  self.b ==1:
                return "i"
            elif self.b==-1:
                return "-i"
            elif self.b ==0 :
                return "0"
            elif self.b>0:
                return str(self.b)+"i"
        elif self.a>0:
            if self.b<0  and self.b!=-1:
                return str(self.a)+str(self.b)+"i"
            elif  self.b ==1:
                return str(self.a)+"+i"
            elif self.b==-1:
                return str(self.a)+"-i"
            elif self.b ==0 :
                return str(self.a)
            else:
                return str(self.a)+"+"+str(self.b)+"i"
        else:
            if self.b<0  and self.b!=-1:
                return str(self.a)+str(self.b)+"i"
            elif  self.b ==1:
                return str(self.a)+"i"
            elif self.b==-1:
                return str(self.a)+"-i"
            elif self.b ==0 :
                return str(self.a)
            else:
                return str(self.a)+"+"+str(self.b)+"i"
    def __add__(self,rhs):
        return Complex(self.a+rhs.a,self.b+rhs.b)
    def __mul__(self,rhs):
        return Complex((self.a*rhs.a)-(self.b*rhs.b),(self.a*rhs.b)+(self.b*rhs.a))
    def __truediv__(self,rhs):
        deno = rhs.a**2+rhs.b**2
        return Complex((self.a*rhs.a+self.b*rhs.b)/deno,((-self.a*rhs.b+self.b*rhs.a)/deno))
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)