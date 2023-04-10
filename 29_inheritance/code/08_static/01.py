
class A:
    shared = 10

    def f(self):
        print(self.shared, A.shared, type(self).shared)

class B(A):
    shared = 5

if __name__ == '__main__':
    b = B()
    b.f()   # 5 10 5
    b.shared = 7
    b.f()   # 7 10 5

    # This is where using self with static vars plays critical role
    # Old tip: Access/modify the class attributes using the Class name
    # Considering inheritance: type(self) plays a good role here
    # Also think if inheritance should have effect or not
    # Note: type(self) is same as self.__class__
    # Better don't access dunder things directly

