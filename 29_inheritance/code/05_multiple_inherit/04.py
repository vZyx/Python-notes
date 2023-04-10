class X4:
    pass


class Z2:
    pass

class Y2(Z2):
    pass

class X3(Y2):
    pass




class X2:
    pass




class Z1:
    pass

class Y1(Z1):
    pass

class X1(Y1):
    pass

class B2(X3, X4):
    pass

class B1(X1, X2):
    pass

class A(B1, B2):
    pass


if __name__ == '__main__':
    print(A.__mro__)
    # A, B1, X1, Y1, Z1, X2, B2, X3, Y2, Z2, X4
