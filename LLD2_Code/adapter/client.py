from payment_adapter import PaymentAdapter
from payment import PaymentStatus, Payment


class PaymentProcessor:
    def __init__(self, payment_provider: PaymentAdapter):
        self.payment_provider = payment_provider


    def process_payment(self):
        self.payment_provider.make_payment()
        status: PaymentStatus = self.payment_provider.get_status("paymentId")
