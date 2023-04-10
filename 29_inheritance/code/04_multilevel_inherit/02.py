

class A:
    def f1(self):
        return 'f1A'
    def f2(self):
        return 'f2A'
    def f3(self):
        return 'f3A'

class B(A):
    def __init__(self):
        super().__init__()
    def f1(self):
        return 'f1B ' + super().f1()
    def f2(self):
        return 'f2B ' + super().f2()

class C(B):
    def __init__(self):
        super().__init__()
    def f1(self):
        return 'f1C ' + super().f1()
    def f3(self):
        return 'f3C ' + super().f3()

if __name__ == '__main__':

    cobj = C()
    print(cobj.f1())
    print(cobj.f2())
    print(cobj.f3())
    # guess output?

"""
f1C f1B f1A
f2B f2A
f3C f3A
"""