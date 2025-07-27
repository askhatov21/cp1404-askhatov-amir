from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    """Test SilverServiceTaxi fare calculation based on fanciness and flagfall."""
    taxi = SilverServiceTaxi("Silver Hummer", fuel=200, fanciness=2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f'Fare: ${fare:.2f}')

    assert abs(fare - 48.78) < 0.01, "Fare should be approximately $48.78"

if __name__ == '__main__':
    test_silver_service_taxi()