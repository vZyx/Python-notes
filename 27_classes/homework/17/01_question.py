

class CarSpecs:
    def __init__(self):
        self.trim = None
        self.engine_type = None
        self.horsepower = None
        self.steering_ratio = None
        # Expected more to be added in future

class AutoTrader:
    def __init__(self):
        self.db_cars_specs = []

    def load_database(self):
        car1 = CarSpecs()
        car1.engine_type = 'EG12121'
        car1.horsepower = 10
        self.db_cars_specs.append(car1)

        car2 = CarSpecs()
        car2.engine_type = 'EG12121'
        car2.horsepower = 12
        self.db_cars_specs.append(car2)
        # Load More

    def get_matches(self, car_specs):
        found = []
        for db_car in self.db_cars_specs:
            if car_specs.trim is not None and car_specs.trim != db_car.trim:
                continue
            if car_specs.engine_type is not None and car_specs.engine_type != db_car.engine_type:
                continue
            if car_specs.horsepower is not None and car_specs.horsepower != db_car.horsepower:
                continue
            if car_specs.steering_ratio is not None and car_specs.steering_ratio != db_car.steering_ratio:
                continue
            found.append(db_car)

        return found


if __name__ == '__main__':
    trader = AutoTrader()
    trader.load_database()

    query = CarSpecs()
    query.engine_type = 'EG12121'

    ans = trader.get_matches(query)
    print(len(ans))     # 2

    query.horsepower = 10
    ans = trader.get_matches(query)
    print(len(ans))     # 1