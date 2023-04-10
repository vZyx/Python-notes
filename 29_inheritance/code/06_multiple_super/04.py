

class A:
    def __init__(self, aval = None):
        print(f'init A: {aval}')
        super().__init__()
        self.aval = aval

class B:
    def __init__(self):
        print('init B')
        super().__init__()

class C(B, A):
    def __init__(self, aval):
        print('init C')
        A.__init__(self, aval)
        B.__init__(self)

print(C.__mro__)    # C, B, A
C(20)

"""
init C
init A: 20
init B
init A: None
"""