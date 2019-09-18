class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        pass

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, days_increase):
        self.day += days_increase
        while self.day > 30:  # assume month is 30 days
            self.month += 1
            self.day -= 30
        while self.month > 12:
            self.year += 1
            self.month -= 12


date = Date(10, 11, 12)
date.add_days(60)
print(date)
