

class ParentA:
    def __init__(self, a):
        self.a = a
        print('init ParentA')

    def fA(self):
        print('fA')


class ParentB:
    def __init__(self, b):
        self.b = b
        print('init ParentB')

    def fB(self):
        print('fB')

class ChildC(ParentA, ParentB):
    def __init__(self, a, b, c):
        ParentA.__init__(self, a)
        ParentB.__init__(self, b)
        self.c = c
        print('init ChildC')

    def fC(self):
        print('fC')

if __name__ == '__main__':
    c = ChildC(1, 3, 5)
    c.fA()
    c.fB()
    c.fC()

"""
init ParentA
init ParentB
init ChildC
fA
fB
fC

"""