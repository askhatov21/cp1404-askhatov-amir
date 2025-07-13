CURRENT_YEAR = 2023
VINTAGE_MINIMUM_YEAR = 50

class Guitar:
    """Represent a guitar """
    def __init__(self, name, year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year} : ${self.cost:,.2f})"


    def __lt__(self, other):
        """Compare guitars by their year of manufacture for sorting."""
        return self.year < other.year

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= VINTAGE_MINIMUM_YEAR


