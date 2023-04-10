"""
- The engineer thought: Square is a rectangle with all sides equal
- This is good for a Square class
- But in practice, some function might set length/witdth and corrupt the object status!

- Tip: Make sure your sub-class is really a valid superclass. This is related to the Liskov Substitution Principle

- The best way is composition
- Square class has an instance of type Rectangle
    - Delegate all calls to a rectangle
    - Now we are safe, without the need for inheritance between rectangle and Square

You can also do inheritance, but with careful coding and using properties. I don't feel it that good way
"""


class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle():
    def __init__(self, height, width):
        self._length = height
        self._width  = width

    def area(self):
        return self._length * self._width

class Square1(Rectangle):   # using inheritance
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self._width

    @side.setter
    def side(self, x):
        self._length = self._width = x

    @property
    def length(self, x):
        raise NotImplementedError

    @property
    def width(self, x):
        raise NotImplementedError


sq = Square1(10)
print(sq.side, sq.area())
sq.side = 12
print(sq.side, sq.area())



class Square2:  # Using composition: like a wrapper class
    def __init__(self, side):
        super().__init__()
        self.rect = Rectangle(side, side)   # Square has a rectangle object

    @property
    def side(self):
        return self.rect.width

    @side.setter
    def side(self, side):
        self.rect = Rectangle(side, side)

    def area(self):
        return self.rect.area() # Delegate the call

sq = Square1(10)
print(sq.side, sq.area())
sq.side = 12
print(sq.side, sq.area())