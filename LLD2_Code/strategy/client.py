from concrete_classes import WalkingStrategy, BikingStrategy, DrivingStrategy
from context_class import NavigatiorContext
from Point_helper_class import Point


def main():
    # choose a strategy
    walking = WalkingStrategy()
    biking = BikingStrategy()
    driving = DrivingStrategy()

    navigator = NavigatiorContext(biking)
    navigator.navigate(Point(2, 3), Point(5, 7))


if __name__ == "__main__":
    main()
