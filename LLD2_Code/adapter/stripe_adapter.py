from stripe_api import StripeApi
from payment_adapter import PaymentAdapter
from payment import Payment, PaymentStatus


class StripeAdapter(PaymentAdapter):
    def __init__(self):
        self.stripe_api = StripeApi()


    def make_payment(self) -> Payment:
        return self.stripe_api.create_payment()


    def get_status(self, payment_id: str) -> PaymentStatus:
        status = self.stripe_api.check_status(payment_id)
        return self.convert_status(status)


    def convert_status(status: str) -> PaymentStatus:
        pass
