from paypal_api import PaypalApi
from payment_adapter import PaymentAdapter
from payment import Payment, PaymentStatus


class PaypalAdapter(PaymentAdapter):
    def __init__(self):
        self.paypal_api = PaypalApi()


    def make_payment(self) -> Payment:
        return self.paypal_api.make_payment()


    def get_status(self, payment_id: str) -> PaymentStatus:
        status = self.paypal_api.get_status(payment_id)
        return self.convert_status(status)


    def convert_status(status: str) -> PaymentStatus:
        pass
