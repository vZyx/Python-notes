
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @abstractmethod
    def get_area(self):
        return -1

class Rectangle(Shape):
    def __init__(self, name, wid, height):
        super().__init__(name)
        self.wid = wid
        self.height = height

# # TypeError: Can't instantiate abstract class
print(Rectangle('Rect', 3, 4).get_area())


