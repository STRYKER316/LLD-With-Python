from abc import ABC, abstractmethod


# Subject class must implement this interface
class ObservableInterface(ABC):
    @abstractmethod
    def add_observer(self, observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass



# Observer class must implement this interface
class ObserverInterface(ABC):
    @abstractmethod
    def update(self) -> None:
        pass
