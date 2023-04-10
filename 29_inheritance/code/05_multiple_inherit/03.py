

class D2:
    pass

class C2(D2):
    def f(self):
        print('C2')

class B2(C2):
    def f(self):
        print('B2')

class D1:
    pass

class C1(D1):
    def f(self):
        print('C1')

class B1(C1):
    pass

class A(B1, B2):
    pass

if __name__ == '__main__':
    print(A.__mro__)
    # A, B1, C1, D1, B2, C2, D2, Object

    A().f() # C1

