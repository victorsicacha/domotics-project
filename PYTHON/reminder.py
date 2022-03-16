from time import *


class Reminder:

    def __init__(self, name: str, description: str, time_of_day: str, repeat=False, days=set({})):
        """The time argument must be in 24hr format, 2 digits for numbers, a colon and two digits for minutes. eg:  \"10:25\."
           The 'days' argument is a set with numbers 1 trough 7 in which each number represents a day of the week. 1 = monday,
           2 = tuesday and so on"""
        self.name = name
        self.description = description
        self.time_of_day = time_of_day
        self.repeat = repeat
        self.days = days

    def editReminder(self, time_of_day: str, repeat=False, days=[]):

        self.time_of_day = time_of_day
        if repeat:
            self.repeat = True
            self.days = days

        return

    def checkRemind(self) -> bool:

        temp = self.time[:2] == strftime("%H") and self.time[3:5] == strftime("%M") # Is the time of the reminder the same as the local time?

        if self.repeat:
            temp = temp and (strftime("%w") in self.days or str(int(strftime("%w")) + 7) in self.days) # Is the local day included in the list of days of the reminder?

        return temp



