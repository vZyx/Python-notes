
class Robot:
    def drive(self):
        pass
    def clean(self):
        pass
    def do_funny_actions(self):
        pass

class RealAnimal:
    def go_toeilt(self):
        pass
    def make_sound(self):
        raise NotImplementedError

class Cat(RealAnimal):
    def make_sound(self):
        print('Meow')

class Dog(RealAnimal):
    def make_sound(self):
        print("Bark")

"""
- If we extended from the 4 classes, we will end up with a lot of functions that are irrelevant to the current class
- Usually, we do mistakes in design and even with a reasonable has-a relationship, a lot of functions just are in our new class that has no use!

- In the example, A robot dog won't go toilet, it is a made dog, not a real one. Sometimes the has-a relationship is not as strong as we wish

"""