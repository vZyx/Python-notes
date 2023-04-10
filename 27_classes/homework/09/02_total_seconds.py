
class Time:
    def __init__(self, hours_or_total_seconds, minutes = None, seconds = None):
        # We can utilize None to figure out which constructor style!

        if minutes is None:
            self.total_seconds = max(0, hours_or_total_seconds)
        else:
            self.total_seconds = 0  # Still outsiders can put -ve value. We can make it property
            self.seconds = seconds  # observe: same name but no cycles, as they depends on total_seconds
            self.minutes = minutes
            self.hours = hours_or_total_seconds


    def get_total_minutes(self):
        return self.minutes

    def get_total_seconds(self):
        return self.total_seconds

    @property
    def seconds(self):
        return self.total_seconds % 60

    @property
    def minutes(self):
        return (self.total_seconds % (60 * 60)) // 60

    @property
    def hours(self):
        return self.total_seconds // (60 * 60)

    @seconds.setter
    def seconds(self, seconds):
        seconds = max(seconds, 0)
        self.total_seconds += seconds - self.seconds

    @minutes.setter
    def minutes(self, minutes):
        minutes = max(minutes, 0)
        self.total_seconds += (minutes - self.minutes ) *60

    @hours.setter
    def hours(self, hours):
        hours = max(hours, 0)
        self.total_seconds += (hours - self.hours) * 60 * 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def __repr__(self):
        return f'Time({self.total_seconds})'




if __name__ == '__main__':
    time = Time(2, 5, 10 + 7 * 60)

    print(str(time))
    print(repr(time))

    print(time.get_total_minutes())
    print(time.get_total_seconds())