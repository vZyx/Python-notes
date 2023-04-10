
class Payment:
    pass

class Card(Payment):
    pass

class CreditCard(Card):
    pass

class DebitCard(Card):
    pass


class Cash(Payment):
    pass

class Cheque(Payment):
    pass


class Order:
    def __init__(self, payment: Payment):
        self.payment = payment



if __name__ == '__main__':
    Order(DebitCard())