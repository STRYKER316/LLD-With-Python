from helper_classes import PaymentGateway, Inventory, EmailService, ShippingService, AnalyticsService


class Order:
    def __init__(self):
        self.payment_gateway = PaymentGateway()
        self.inventory = Inventory()
        self.email_service = EmailService()
        self.shipping_service = ShippingService()
        self.analytics_service = AnalyticsService()


    def checkout(self):
        self.payment_gateway.charge()
        self.inventory.update()
        self.email_service.send()
        self.shipping_service.add()
        self.analytics_service.update()
