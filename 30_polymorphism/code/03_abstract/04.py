
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, wid, height):
        super().__init__(name)
        self.wid = wid
        self.height = height

    @property
    def area(self):
        return self.wid * self.height

print(Rectangle('Rect', 3, 4).area)   # 12


