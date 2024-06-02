class Fraction:
    def __init__(self,n,d):
        self.nom=n
        self.denom=d
    def __str__(self):
        return "{}/{}".format(self.nom,self.denom)
    def __add__(self, other):
        resnom=self.nom*other.denom+other.nom*self.denom
        resdenom=self.denom*other.denom
        return "{}/{}".format(resnom, resdenom)
    def __sub__(self, other):
        resnom=self.nom*other.denom-other.nom*self.denom
        resdenom=self.denom*other.denom
        return "{}/{}".format(resnom, resdenom)
    def __mul__(self, other):
        mulnom=self.nom*other.nom
        muldenom=self.denom*other.denom
        return "{}/{}".format(mulnom, muldenom)
    def __truediv__(self,other):
        divnom=self.nom*other.denom
        divdenom=self.denom*other.nom
        return "{}/{}".format(divnom,divdenom)
a=Fraction(2,3)     
print(a)
b=Fraction(4,5)
print(b)
print("Addition of two fractions a and b is:       ",a+b)
print("subraction of two fractions a and b is:     ",a-b)
print("Multiplication of two fractions a and b is: ",a*b)
print("Division of two fractions a and b is:       ",a/b)