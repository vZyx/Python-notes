"""
Every API has its own attributes and methods, although share same functionality

Our code base can't depend on one specific API. Otherwise, once we change it, we change all our code!

Define an interface to be unifed. Our codebase depends on it only. This is called loose coupling (means our code is not tight to something).
    Tip: This is very critical in other languages such as Java and C#


"""


from abc import ABC, abstractmethod

class IPayment(ABC):    # I for interface
    @abstractmethod
    def set_user_info(self, name, address):
        pass

    @abstractmethod
    def set_card_info(self, id, expire_date, ccv):
        pass
    
    @abstractmethod
    def make_payment(self, money):
        pass
    

class PayPalCreditCard:
    def __init__(self, name = None, address= None,
          id= None, expire_date= None, ccv= None):
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv


class PayPalOnlinePaymentAPI:
    def __init__(self, card_info : PayPalCreditCard = None):
        self.card_info = None

    def pay_money(self, money):
        print(f'PayPalOnlinePaymentAPI request')
        return True # Call PayPal backend
    
class StripeUserInfo:
    def __init__(self, name = None, address = None):
        self.name = name
        self.address = address


class StripeCardInfo:
    def __init__(self, id = None, expire_date = None):
        self.id = id
        self.expire_date = expire_date


class StripePaymentAPI:
    @staticmethod
    def withdraw_money(user_info, card_info, money):
        print(f'StripePaymentAPI request')
        return True # Call Stripe backend

##########
# Implement our own classes that wrap the APIs and following the payment interface

class PayPalPayment(IPayment):
    def __init__(self):
        self.paypal = PayPalOnlinePaymentAPI()
        self.card = PayPalCreditCard()

    def set_user_info(self, name, address):
        self.card.name = name
        self.card.address = address

    def set_card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.card.ccv = ccv

    def make_payment(self, money):
        self.paypal.card_info = self.card
        return self.paypal.pay_money(money)


class StripePayment(IPayment):
    def __init__(self):
        self.card = StripeCardInfo()
        self.user = StripeUserInfo()

    def set_user_info(self, name, address):
        self.user.name = name
        self.user.address = address

    def set_card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.card.ccv = ccv

    def make_payment(self, money):
        return StripePaymentAPI.withdraw_money(self.user, self.card, money)

############
# Create our side code depending on the interface NOT on an API that may change soon

class TransactionInfo:
    def __init__(self, required_money_amount, name, address, id, expire_date, ccv):
        self.required_money_amount = required_money_amount
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv


class Craigslist:   # This class depends on IPayment. No idea about Paypal/Stripe/Whatever
    def __init__(self, payment: IPayment):
        self.payment = payment

    def do_payment(self, info: TransactionInfo):
        self.payment.set_user_info(info.name, info.address)
        self.payment.set_card_info(info.id, info.expire_date, info.ccv)

        return self.payment.make_payment(info.required_money_amount)
    



if __name__ == '__main__':
    #site = Craigslist(StripePayment())
    site = Craigslist(PayPalPayment())

    info = TransactionInfo(20.5, "mostafa", "canada", "11-22-33-44", "09-2021", 333)

    site.do_payment(info)

