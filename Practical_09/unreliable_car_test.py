from unreliable_car import UnreliableCar
import random

def test_unreliable_car():
    """Test the functionality of the Unreliable Car"""

    random.seed(99) # for reproducibility

    reliable_car = UnreliableCar("ReliableCar", fuel=1000, reliability=90)
    unreliable_car = UnreliableCar("UnreliableCar", fuel=1000, reliability=30)

    reliable_success = 0
    unreliable_success = 0
    test_runs = 100

    for _ in range(test_runs):
        if reliable_car.drive(1) > 0:
            reliable_success += 1
            if unreliable_car.drive(1) > 0:
                unreliable_success += 1

    print(f"Reliable drove successfully {reliable_success} times out of {test_runs}")
    print(f"UnreliableCar drove successfully {unreliable_success} times out of {test_runs}")

    assert reliable_success > unreliable_success, "ReliableCar should drive more often than UnreliableCar"
    assert 70 <= reliable_success <= 100, "ReliableCar should drive most of the time"
    assert 0 <= unreliable_success <= 50, "UnreliableCar should often fail to drive"

if __name__ == '__main__':
    test_unreliable_car()