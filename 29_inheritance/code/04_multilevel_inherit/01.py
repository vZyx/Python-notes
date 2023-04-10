

class A:
    def __init__(self):
        print('init A', self)
    def f1(self):
        print('f1A ')
    def f2(self):
        print('f2A ')
    def f3(self):
        print('f3A ')

class B(A):
    def __init__(self):
        super().__init__()
        print('init B', self)
    def f1(self):
        print('f1B ')
    def f2(self):
        print('f2B ')

class C(B):
    def __init__(self):
        super().__init__()
        print('init C', self)
    def f1(self):
        print('f1C ')


if __name__ == '__main__':

    cobj = C()
    cobj.f1()
    cobj.f2()
    cobj.f3()
    # Guess output!

"""
init A <__main__.C object at 0x7fa42f069850>
init B <__main__.C object at 0x7fa42f069850>
init C <__main__.C object at 0x7fa42f069850>
f1C 
f2B 
f3A 

Observe: self is bound to cobj all the time!
    The created object
So any method call is bound to cobj all time

Many errors will be resolved by remembering that!
"""