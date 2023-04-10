

class A:
    def f3(self):
        return 'f3A ' + self.f4()
        #return 'f3A' + super().f4()

class B(A):
    def f2(self):
        return 'f2B ' + super().f3()

class C(B):
    def __init__(self):
        super().__init__()

    def f1(self):
        return 'f1C ' + self.f2()

    def f3(self):
        return super().f3() + '\t' + 'C - f3'

    def f4(self):
        return 'f4C '


if __name__ == '__main__':
    print(C().f1())     # f1C f2B f3A f4C
    #print(B().f2())   B has no attribute f4

    # self/methods/attributes bound to the
    # CALLING INSTANCE not current class
