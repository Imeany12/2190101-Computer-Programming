class Complex :
    
    def __init__(self,a,b) :

        self.real = a
        self.complex = b

    def __str__(self) :
        if self.real != 0 :
            if self.complex == 0 :
                return self.real
            elif self.complex > 0 :
                if self.complex == 1 :
                    return str(self.real) + "+" + "i"
                else : return str(self.real) + "+" + str(self.complex) + "i"
            else :
                if self.complex == -1 :
                    return str(self.real) + "-" + "i"
                else : return str(self.real) + str(self.complex) + "i"
        else :
            if self.complex == 0 :
                return "0"
            elif self.complex > 0 :
                if self.complex == 1 :
                    return "i"
                else : return str(self.complex) + "i"
            else :
                if self.complex == -1 :
                    return "-" + "i"
                else : return str(self.complex) + "i"

    def __add__(self,rhs) :

        totalreal = self.real + rhs.real
        totalcomplex = self.complex + rhs.complex
        return Complex(totalreal,totalcomplex)

    def __mul__(self,rhs) :

        totalreal = self.real*rhs.real - self.complex*rhs.complex
        totalcomplex = self.complex*rhs.real + rhs.complex*self.real
        return Complex(totalreal,totalcomplex)

    def __truediv__(self,rhs) :
        totalreal = ((self.real*rhs.real)+(self.complex*rhs.complex))/(rhs.real**2+rhs.complex**2)
        totalcomplex = (-(self.real*rhs.complex)+(self.complex*rhs.real))/(rhs.real**2+rhs.complex**2)
        return Complex(totalreal,totalcomplex)

t,a,b,c,d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 :print(c1)
elif t==2 : print(c2)
elif t==3 : print(c1+c2)
elif t==4 : print(c1*c2)
else : print(c1/c2)
