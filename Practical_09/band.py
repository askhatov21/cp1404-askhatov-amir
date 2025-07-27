from musician import Musician


class Band:
    """Band class to manage multiple Musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Tell each musician in the band to play."""
        for musician in self.musicians:
            musician.play()