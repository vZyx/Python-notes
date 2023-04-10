

class A:
        print('init A')

class B(A):
    def __init__(self):
        print('init B')

class C(A, B):
    def __init__(self):
        print('init D')


C()
"""
TypeError: Cannot create a consistent 
method resolution order (MRO) for bases A, B


Note: class C(B, A):
    will work
"""