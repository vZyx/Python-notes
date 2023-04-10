
# 1e-10 = 0.0000000001

from functools import total_ordering

@total_ordering
class MyFloat(float):
    def __eq__(self, other, eps = 1e-10):
        # float is an approximation. If 2 values are equal, the difference should be very small (e..g epsilon)
        # This code educational purpose to understand only. See link below
        return abs(self - other) < eps

    def __lt__(self, other):
        if self == other:
            return False
        return self < other


# Future reading https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python


if __name__ == '__main__':
    f1 = 1 + 3/7 -1
    f2 = 3/7

    # False 0.4285714285714286 0.42857142857142855
    print(f1 == f2, f1, f2)

    f1 = MyFloat(f1)
    f2 = MyFloat(f2)
    print(f1 == f2) # True
    print(f1 < f2)  # False
    print(f1 >= f2) # True

