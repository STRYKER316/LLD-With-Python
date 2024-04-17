from interfaces import Observable, ObserverInterface


# Implementation of the Observable interface
class BitcoinTracker(Observable):
    def __init__(self):
        self._price = 0
        self._observers = []

    # BitcoinTracker methods -> Getters and Setters
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price
        self.notify_observers()

    # Observable methods
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()


# Implementation of the Observer interface
class EmailNotifier(ObserverInterface):
    def __init__(self, BitcoinTracker):
        self._BitcoinTracker = BitcoinTracker

    def update(self):
        price = self._BitcoinTracker.get_price()
        print(f"Email Notification: Bitcoin price has changed to {price}")

