import math

class Fraction :
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def compact(self) :
        k = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / k)
        self.denominator = int(self.denominator / k)
    def output(self) :
        print(self.numerator, "/", self.denominator, sep = "")
    def sum_fraction(self, fraction) :
        self.numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        self.compact()
        print(self.numerator, "/", self.denominator, sep = "")

a, b, c, d = [int(x) for x in input().split()]
f = Fraction(a, b)
fo = Fraction(c, d)
f.compact()
fo.compact()
f.sum_fraction(fo)