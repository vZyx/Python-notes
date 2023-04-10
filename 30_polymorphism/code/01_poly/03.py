
class Shape:
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, name, wid, height):
        super().__init__(name)
        self.wid = wid
        self.height = height

    @property
    def area(self):
        return self.wid * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    @property
    def area(self):
        from math import pi
        return 2 * pi * self.radius

class Editor:
    def __init__(self):
        self.shapes = []

    def process(self):
        area_sum = 0
        for shape in self.shapes:
            print(shape.name, shape.area)
            area_sum += shape.area
        return area_sum

if __name__ == '__main__':
    editor = Editor()
    editor.shapes.append(Rectangle('Rect1', 3, 5))
    editor.shapes.append(Circle('MyCirc', 2))
    editor.shapes.append(Rectangle('Rect2', 10, 2))
    print(f'area sum = {editor.process()}')