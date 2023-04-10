
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @abstractmethod
    def get_area(self):
        pass


# TypeError: Can't instantiate abstract class .
# Shape with abstract methods get_area
Shape('')


