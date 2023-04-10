

class A:
    def __init__(self, aval):
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