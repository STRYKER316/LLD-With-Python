from strategy_interface import NavigationStrategy
from Point_helper_class import Point


class NavigatiorContext:
    def __init__(self, strategy: NavigationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NavigationStrategy):
        self._strategy = strategy

    def navigate(self, startPoint: Point, endPoint: Point):
        self._strategy.navigate(startPoint, endPoint)
