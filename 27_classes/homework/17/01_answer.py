class CarSpecs:
    def __init__(self, **kwargs):
        # Now the init is both useful and more generic
        self.__dict__.update(kwargs)
        # Reading: https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python

    # It was bad to force other classes to keep get/compare the class field
    # “Don’t ask for the information you need to do the work; ask the object that has the information to do the work for you.” Allen Holub
    # is_match is better encapsulation
    # from Future code changes perspective: with more attributes, outsiders has minimum to zero changes
    def is_match(self, query_car):
        # iterate on the available query attributes and compare over them
        for key, value in query_car.__dict__.items():
            if self.__dict__[key] != value:
                return False
        return True


class AutoTrader:
    def __init__(self):
        self.db_cars_specs = []

    def load_database(self):
        self.db_cars_specs.append(CarSpecs(engine_type='EG12121', horsepower=10))
        self.db_cars_specs.append(CarSpecs(engine_type='EG12121', horsepower=12))
        self.db_cars_specs.append(CarSpecs(horsepower=15))
        # Load More

    def get_matches(self, query_car_specs):
        # short, elegant and doesn't depend on # of features
        return [db_car for db_car in self.db_cars_specs if db_car.is_match(query_car_specs)]


if __name__ == '__main__':
    trader = AutoTrader()
    trader.load_database()

    ans = trader.get_matches(CarSpecs(engine_type = 'EG12121'))
    print(len(ans))     # 2

    ans = trader.get_matches(CarSpecs(engine_type='EG12121', horsepower = 10))
    print(len(ans))     # 1