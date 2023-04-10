

class Car:
    def __init__(self, name, model):
        self.name = name
        self.engine = self.Engine(model)
    def __repr__(self):
        return f'Name: {self.name} - {self.engine}'

    class Engine:
        def __init__(self, model):
            self.model = model
        def __repr__(self):
            return f'{self.__class__.__name__} Model: {self.model}'
            #return f'{type(self).__name__} Model: {self.model}'

if __name__ == '__main__':
    car = Car('bmw', 'LD1102334')
    print(car)      # Name: bmw - Engine Model: LD1102334

    engine = Car.Engine('NEWXX')
    print(engine)   # Engine Model: NEWXX

    setattr(engine, 'release_year', 2021)
    print(engine.release_year)  # also there is getattr
