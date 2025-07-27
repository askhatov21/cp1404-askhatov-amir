from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """ A more luxurious version of a Taxi with higher fare and flagfall."""
    flagfall = 4.50 # fixed extra change per fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServicetaxi with fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the fare for the trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string with fare details and flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"