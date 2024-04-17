from strategy_interface import NavigationStrategy
from Point_helper_class import Point


# Starategy 1
class WalkingStrategy(NavigationStrategy):
    def navigate(self, startPoint: Point, endPoint: Point) -> None:
        print(f"Navigation from {startPoint} to {endPoint} using walking")


# Starategy 2
class BikingStrategy(NavigationStrategy):
    def navigate(self, startPoint: Point, endPoint: Point) -> None:
        print(f"Navigation from {startPoint} to {endPoint} using biking")


# Starategy 3
class DrivingStrategy(NavigationStrategy):
    def navigate(self, startPoint: Point, endPoint: Point) -> None:
        print(f"Navigation from {startPoint} to {endPoint} using driving")
