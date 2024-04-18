from abc import ABC, abstractmethod
from payment import Payment, PaymentStatus


class PaymentAdapter(ABC):
    @abstractmethod
    def make_payment(self) -> Payment:
        pass

    @abstractmethod
    def get_status(self, payment_id: str) -> PaymentStatus:
        pass
