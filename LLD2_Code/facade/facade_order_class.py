from complex_order_processor_class import OrderProcessor


class Order:
    def __init__(self, order_processor: OrderProcessor):
        self.order_processor = order_processor


    def checkout(self):
        self.order_processor.process()
