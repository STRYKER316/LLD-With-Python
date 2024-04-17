from abc import ABC, abstractmethod
from Point_helper_class import Point


# Interface to be implemented by cincrete classes
class NavigationStrategy(ABC):
    @abstractmethod
    def navigate(self, startPoint: Point, endPoint: Point) -> None:
        pass
