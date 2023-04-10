
class Shape:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def print(self):
        print(self.name, self.area)

class Rectangle(Shape):
    def __init__(self, name, wid, height):
        super().__init__(name)
        self.wid = wid
        self.height = height

    @property
    def area(self):
        return self.wid * self.height

if __name__ == '__main__':
    Rectangle('Rect1', 3, 5).print()

