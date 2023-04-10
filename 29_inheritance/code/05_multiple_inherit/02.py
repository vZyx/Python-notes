

class ParentA:
    def f(self):
        print('ParentA')

class ParentB:
    def f(self):
        print('ParentB')

class ChildC1(ParentA, ParentB):
    pass

class ChildC2(ParentB, ParentA):
    pass

if __name__ == '__main__':
    print(ChildC1.__mro__)  # (ChildC1, ParentA, ParentB, object)

    print(ChildC2.__mro__)  # (ChildC2, ParentB, ParentA, object)
    ChildC2().f()           # ParentB is the left one
