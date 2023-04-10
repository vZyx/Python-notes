
class DateTime:
    def __init__(self, day, month, year,
                 hours, minutes, second):
        self.day = day
        self.month = month
        self.year = year
        self.hours = hours
        self.minutes = minutes
        self.second = second

    # Many methods about date

    # Many methods about time





"""
The problem with above class it is responsible for 2 things
    Date and all its complications
    Time and all its complications
    
Always focus a class on a specific functionality (single responsibility)
    Then, each class is easier to code
    Easy to give different developers different tasks
    
This is called single responsibility principle!

Better approach
"""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Time:
    def __init__(self, hours, minutes, second):
        self.hours = hours
        self.minutes = minutes
        self.second = second


class DateTime:
    def __init__(self, day, month, year,
                 hours, minutes, second):
        self.date = Date(day, month, year)
        self.time = Date(hours, minutes, second)

        # This is called composition
        # Datetime class is composed of other 2 objects: date and time

        # Other example: Car is composed of an enginer