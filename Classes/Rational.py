class Rational:

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "( {0} / {1} )".format(self.numerator,self.denominator)
    
r = Rational(4,5)
print(r)

