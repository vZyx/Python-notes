


class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        # super()
        super(B, self).__init__()
        # <class 'super'>
        print(type(super(B, self)))
        print(type(super()))
        print('B')

B()