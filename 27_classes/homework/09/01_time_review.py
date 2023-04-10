

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_total_minutes(self):
        return self.hours * 60 + self.minutes

    def get_total_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


if __name__ == '__main__':
    time = Time(0, 0, 10 * 60 + 3)
    print(time)

"""
1- Code Readability: In line 5: it might be better to make line for each.

2- get_total_seconds better call get_total_minutes: e.g. return self.get_total_seconds() * 60 + self.seconds

3- You should provide repr method at least. This covers calls from repr and str. If intend different printings, provide both

4- In str: we better format the output in 2 digits. E.g. 02:03:37 rather than 2:3:37

5- In line 18: what if more seconds are provided? User will expect a handling?

6- The user might provide a negative value, but we may assume some responsibility. The important part our code doesn't crash.

"""