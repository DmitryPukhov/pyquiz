class DayOfTheWeek:
    """
    Given a date, return the corresponding day of the week for that date.

    The input is given as three integers representing the day, month and year respectively.

    Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



    Example 1:

    Input: day = 31, month = 8, year = 2019
    Output: "Saturday"
    Example 2:

    Input: day = 18, month = 7, year = 1999
    Output: "Sunday"
    Example 3:

    Input: day = 15, month = 8, year = 1993
    Output: "Sunday"
    """

    def isleap(self, year: int):
        """
        if (year is not divisible by 4) then (it is a common year)
        else if (year is not divisible by 100) then (it is a leap year)
        else if (year is not divisible by 400) then (it is a common year)
        else (it is a leap year)
        :param year:
        :return:
        """
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True

    def leaps(self, year):
        """
        Calc leap years up to given, excluding given
        """
        year -= 1
        l0 = 1971 // 4 - (1971 // 100 - 1971 // 400)
        return year // 4 - (year // 100 - year // 400) - l0

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # Start from 1971, so reset year
        dyear = year - 1970

        # Days in prev years
        prevy = abs(dyear - 1)
        l = self.leaps(year)
        prevyd = prevy * 365 + l  # Compensate 1972 leap year

        # Days in prev months of the year
        mdd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isleap(year):
            mdd[1] = 29
        prevmd = sum(mdd[0:abs(month - 1)])

        # Total days
        days = prevyd + prevmd + day

        # Week day
        # From 1.1.1971
        wdays = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        wd = (days - 1) % 7
        return wdays[wd]

