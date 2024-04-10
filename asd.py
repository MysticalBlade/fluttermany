class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

workday = Duration(10, 30)
monday_time = Duration(10, 0)
tuesday_time = Duration(11, 30)
wednesday_time = Duration(5, 45)

print(monday_time < workday)
print(tuesday_time < workday)
print(wednesday_time < workday)
print(monday_time < wednesday_time)