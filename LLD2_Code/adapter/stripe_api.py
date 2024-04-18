from payment import Payment, PaymentStatus


class StripeApi:
    def create_payment(self) -> Payment:
        # Create payment
        pass

    def check_status(self, payment_id: str) -> PaymentStatus:
        # Check payment status
        pass
