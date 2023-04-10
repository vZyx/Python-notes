

class FourWheels:
    # Some variables and methods
    pass

class Engine:
    # Some variables and methods
    pass

class Car(Engine, FourWheels):
    # Some variables and methods
    pass

"""
The semantic is wrong. There is no clear and strong has-a relationship. Never do that in inheritance

A car is not an Engine. The car is not 4 wheels. 

Sometimes we can stack things with inheritance and it works for now (and be a big mess later)

The right relationship is composition. The car has an engine and 4-wheels

Prefer composition over inheritance most of the time, even if inheritance makes more sense unless it really should be an inheritance. Think twice.
"""

class Car2:
    def __init__(self):
        # Car has an engine
        # Car is composed of 4 wheels
        self.wheels = FourWheels()
        self.engine = Engine()

    def something(self):
        # Use engine and wheels
        pass