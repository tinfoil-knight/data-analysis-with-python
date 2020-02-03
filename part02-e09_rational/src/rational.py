#!/usr/bin/env python3

class Rational(object):

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    
    def __add__(x, y):
        term1 = x.b * y.b
        term2 = (x.a * y.b) + (y.a * x.b) 
        return Rational(term2, term1)
        
    def __sub__(x, y):
        term1 = x.b * y.b
        term2 = (x.a * y.b) - (y.a * x.b)
        return Rational(term2, term1)

    def __mul__(x, y):
        return Rational((x.a*y.a),(x.b*y.b))
    
    def __truediv__(x, y):
        return (Rational((x.a*y.b),(x.b*y.a)))

    def __eq__(x, y):
        if x.a == y.a and x.b == y.b:
            return True
        else:
            return False

    def __gt__(x, y):
        if x.b != y.b:
            if (x.a * y.b) > (y.a * x.b):
                return True
            else: 
                return False
        else: 
            if x.a > y.a:
                return True
            else:
                return False 
    
    def __lt__(x, y):
        if x.b != y.b:
            if (x.a * y.b) < (y.a * x.b):
                return True
            else: 
                return False
        else: 
            if x.a < y.a:
                return True
            else:
                return False

    def __str__(self):
        return f'{self.a}/{self.b}'

    
    pass

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

# MY INITIAL CRAP
# class Rational(object):
#     def __init__(self, num1, num2):
#         self.a = num1
#         self.b = num2
#         self.num = self.num1/self.num2
#     def __add__(self, y):
#         return self.num + y.num
#     def __sub__(self, y):
#         return self.num - y.num
#     def __mul__(self, y):
#         return self.num * y.num
#     def __truediv__(self, y):
#         return self.num / y.num
    
#     def __eq__(self, y):
#         return self.num == y.num
#     def __gt__(self, y):
#         return self.num > y.num
#     def __lt__(self, y):
#         return self.num < y.num

#     def __str__(self):
#         return f"{self.num1/self.num2}"

#MODEL SOLUTIOM
#!/usr/bin/env python3
 
# class Rational(object):
#     def __init__(self, n, d):
#         self.n = n
#         self.d = d
 
#     def __str__(self):
#         return "%i/%i" % (self.n, self.d)
 
#     def __repr__(self):
#         return "Rational(%i, %i)" % (self.n, self.d)
 
#     def __mul__(self, r2):
#         a = self.n * r2.n
#         b = self.d * r2.d
#         return Rational(a,b)
 
#     def __truediv__(self, r2):
#         a = self.n * r2.d
#         b = self.d * r2.n
#         return Rational(a,b)
 
#     def __add__(self, r2):
#         d1 = self.d
#         d2 = r2.d
#         a = self.n * d2 + r2.n * d1
#         b = d1 * d2
#         return Rational(a, b)
 
#     def __sub__(self, r2):
#         d1 = self.d
#         d2 = r2.d
#         a = self.n * d2 - r2.n * d1
#         b = d1 * d2
#         return Rational(a, b)
 
#     def __eq__(self, r2):
#         return self.n * r2.d == self.d *r2.n
 
#     def __lt__(self, r2):
#         return self.n * r2.d < self.d *r2.n
 
#     def __gt__(self, r2):
#         return self.n * r2.d > self.d *r2.n
 
# def main():
#     r1=Rational(1,4)
#     r2=Rational(2,3)
#     print(r1)
#     print(r2)
#     print(r1*r2)
#     print(r1/r2)
#     print(r1+r2)
#     print(r1-r2)
#     print(Rational(1,2) == Rational(2,4))
#     print(Rational(1,2) > Rational(2,4))
#     print(Rational(1,2) < Rational(2,4))
 
# if __name__ == "__main__":
#     main()