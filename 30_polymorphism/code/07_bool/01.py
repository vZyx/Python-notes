
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __add__(self, other):
        return MyPair(self.first  + other.first,
                      self.second + other.second)

    def __bool__(self):
        if self.first == 0 and self.second == 0:
            return False
        return True
        # It should return bool, e.g. NOT
        # return self.first and self.second
if __name__ == '__main__':
    print(bool(MyPair(2, 3)))      # True
    print(bool(MyPair(2, 0)))      # True
    print(bool(MyPair(0, 0)))      # False

