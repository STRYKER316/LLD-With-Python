from payment import Payment, PaymentStatus


class PayPalApi:
    def make_payment(self) -> Payment:
        # Create payment
        pass

    def get_status(self, payment_id: str) -> PaymentStatus:
        # Check payment status
        pass
