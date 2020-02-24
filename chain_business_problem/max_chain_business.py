class Business():
    def __init__(self, name, location, _id):
        """Inititlize the obeject with name, location, and
        _id attributes
        """
        self.name = name
        self.location = location
        self._id = _id

    def __repr__(self):
        """String representation of the object"""
        return (f"name: {self.name}, location: {self.location}, id: {self._id}")





businesses = [
    Business("Sturbucks", "SF", 100),
    Business("Sturbucks", "SF", 100),
    Business("Whole Foods", "SF", 101),
    Business("Whole Foods", "SF", 102),
    Business("Amazon", "SF", 103),
    Business("Amazon", "SF", 110),
    Business("McDonalds", "SF", 104),
    Business("McDonalds", "SF", 104),
    Business("McDonalds", "NYC", 106),
    Business("McDonalds", "NYC", 105)
]

# obj = Business()

