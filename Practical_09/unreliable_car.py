import random
from car import Car

class UnreliableCar(Car):
    """An unreliable car that may not drive when asked."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with reliability as percentage"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car, but may fail based on reliability."""
        if random.uniform(0, 100) < self.reliability:
            # Reliable enough - car drives
            return super().drive(distance)
        else:
            # Unreliable - car doesn't move
            print(f"{self.name} refused to drive (reliability {self.reliability:.1f}%)")
            return 0
