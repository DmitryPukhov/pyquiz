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
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day -= 1
        month -= 1

        # year days
        yd = 0
        for i in range(1, year):
            yd += 365
            if self.isleap(i):
                yd += 1

        # month days
        mdd = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isleap(year):
            mdd[1] = 29
        md = sum(mdd[0:month])

        # Total days
        days = yd + md + day

        # Week day
        wdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        wd = days % 7
        return wdays[wd]


# day = 1
# month = 2
# year = 2020
# print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')


# day = 1
# month = 1
# year = 2000
# print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')
#
# day = 1
# month = 21
# year = 2001
# print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')
#
# day = 31
# month = 8
# year = 2019
# print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')
#
# day = 16
# month = 1
# year = 2020
# print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')
#
day = 1
month = 1
year = 0
print(f'{day}.{month}.{year} is {DayOfTheWeek().dayOfTheWeek(day, month, year)}')
