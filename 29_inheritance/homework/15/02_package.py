

class Address:
    def __init__(self, name, street_address, city):
        super().__init__()
        self.name = name
        self.street_address = street_address
        self.city = city

class StandardPackage:
    def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg):
        super().__init__()
        self.sender_address = sender_address
        self.reciever_address = reciever_address
        self.weight_kg = weight_kg
        self.price_per_kg = price_per_kg

    def total_cost(self):
        return self.weight_kg * self.price_per_kg

class TwoDayPackage(StandardPackage):
    def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg, fixed_fee):
        super().__init__(sender_address, reciever_address, weight_kg, price_per_kg)
        self.fixed_fee = fixed_fee

    def total_cost(self):
        return self.fixed_fee + super().total_cost()

class HeavyPackage(StandardPackage):
    weight_limit = 100

    def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg, extra_price_per_kg):
        super().__init__(sender_address, reciever_address, weight_kg, price_per_kg)
        self.extra_price_per_kg = extra_price_per_kg

    def total_cost(self):
        res  = super().total_cost()

        if self.weight_kg > self.weight_limit:
            res += (self.weight_kg - self.weight_limit) * self.extra_price_per_kg

