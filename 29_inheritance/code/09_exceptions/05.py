



class PaymentBaseException(BaseException):
    pass

class NegativePaymentException(PaymentBaseException):
    def __init__(self, money, message = 'Paid amount must be positive'):
        self.money = money
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.money} amount caused error. \n\tSee: {self.message}'


raise NegativePaymentException(-20)

"""
__main__.NegativePaymentException: -20 amount caused error. 
	See: Paid amount must be positive
"""

