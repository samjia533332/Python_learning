def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        neg = 1
        if newnum < 0 :
            neg = -1
        newnum = newnum * neg
        common = gcd(newnum,newden)
        return Fraction(neg*newnum/common, newden/common)

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        neg = 1
        if newnum*newden < 0 :
            neg =-1
        if newnum < 0 : 
            newnum = -1*newnum
        if newden < 0 :
            newden = -1*newden
        common = gcd(newnum, newden)
        return Fraction(newnum/common,newden/common)

    def __truediv__(self, other):
        pass

    def __gt__(self, other):
        pass
    
    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ne__(self, other):
        pass



if __name__=="__main__":
    x = Fraction(1,2)
    y = Fraction(2,3)
    print(x+y)
    print(x == y)
    print(x)
    print(y)
    # test sub function
    # 1 2/3-1/2
    print(y-x)
    # test negative restult
    print(x-y)
    # test common denominator sub
    z = Fraction(3,4)
    z1 = Fraction(1,4)
    print (z-z1)
    print (z1-z)
    print (x*y)
    #
    print (x*y)
    x1 = Fraction(-1,2)
    x2 = Fraction(-2,3)
    print (x1*x2)
