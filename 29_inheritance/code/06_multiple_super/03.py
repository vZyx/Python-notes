

class A:
    def __init__(self):
        #super().__init__()
        print('init A')

class B(A):
    def __init__(self):
        print('init B')
        super().__init__()

class C:
    def __init__(self):
        print('init C')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('init D')
        super().__init__()

print(D.__mro__)    # D, B, A, C
D()     # Guess the output

"""
init D
init B
init A
"""