class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = int(cost)

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - int(self.year)

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
