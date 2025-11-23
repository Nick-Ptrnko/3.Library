#%%
class TimeRange:
    def __init__(self, time_start: tuple, time_end: tuple):
        self.hours, self.minutes, self.seconds = time_start
        self.time_end = time_end
    def __iter__(self):
        return self
    def __next__(self):
        if self.seconds >= 59:
            self.seconds = 0
            self.minutes += 1
        elif self.minutes >= 59:
            self.minutes = 0
            self.hours += 1
        elif self.hours >= 23:
            self.hours = 0
        self.seconds += 1
        return (self.hours, self.minutes, self.seconds)
t_rang = TimeRange(time_start=(10, 0, 0), time_end=(10, 0, 3))

next(t_rang)