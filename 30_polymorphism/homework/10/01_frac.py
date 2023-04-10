
from functools import total_ordering
import math

@total_ordering
class Fraction:
    def __init__(self, num, den = 1):
        assert isinstance(num, int)
        assert isinstance(den, int)

        g = math.gcd(num, den)
        num //= g
        den //= g

        self.num = num
        self.den = den

    def __eq__(self, other):
        return (self.num, self.den) == (other.num, other.den)

    @property
    def value(self):
        if self.den == 0:
            return None
        return self.num / self.den

    def __repr__(self):
        if self.den != 1:
            return f'{self.num}/{self.den}'
        return f'{self.num}'

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return False

        if self == other:
            return False

        if self.den == other.den:
            return self.num < self.den

        a, b = self.value, other.value
        if a is None:
            return False
        if b is None:
            return True
        return a < b


    def __mul__(self, other):
        if not isinstance(other, Fraction):
            if not isinstance(other, int):
                return NotImplemented
            return self * Fraction(other)

        return Fraction(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self * Fraction(other)


if __name__ == '__main__':


    f1 = Fraction(4, 8)
    print(f1)       # 1/2
    print(f1 * f1)  # 1/4

    f1 = Fraction(3, 8)
    f2 = 2 * f1
    f3 = f1 * Fraction(5, 4) * 16
    print(f1, f2, f3)
    # 3/8 3/4 15/2

    print(f1 == f2) # False
    print(f2 > f1)  # True
    print(f1.value) # 0.375
