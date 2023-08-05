from calendar import Calendar
import datetime

from canada_holiday.utils import (
    DAY_TO_INDEX,
    find_easter_day,
    get_day_of_the_week_idx,
    get_last_day_str_of_month,
    parse_preceding_day_str,
)

cal = Calendar()


class CanadaHoliday:
    def __init__(
        self,
        name: str,
        month: int,
        year: int = None,
        day: int = None,
        day_of_the_week: str = None,
        date: datetime.date = None,
        nearest_day: (str, int) = None,
        nth_day: (str, int) = None,
        preceding_date: (str, int) = None,
        province: str = None,
        succeeding_date: (str, int) = None,
    ):
        self.name = name
        self.month = month
        self.year = year
        self.day = day
        self._day_of_the_week = day_of_the_week
        self._date = date  # ex: datetime.date(2023, 12, 25)
        self.nearest_day = nearest_day
        self.nth_day = nth_day
        self.preceding_date = preceding_date
        self.province = province
        self.succeeding_date = succeeding_date

        self.validate_holiday_condition()

    def __repr__(self):
        return f"CanadaHoliday({self.name}, {self.date}, {self.day_of_the_week}, {self.province})"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: datetime.date):
        self._date = date

    @property
    def day_of_the_week(self):
        return self._day_of_the_week

    @day_of_the_week.setter
    def day_of_the_week(self, day_of_the_week: str):
        self._day_of_the_week = day_of_the_week

    def validate_holiday_condition(self) -> None:
        invalid = False
        if self.nth_day:
            invalid = any([self.preceding_date, self.succeeding_date, self.nearest_day])
        elif self.nearest_day:
            invalid = any([self.nth_day, self.preceding_date, self.succeeding_date])
        elif self.preceding_date:
            invalid = any([self.nth_day, self.succeeding_date, self.nearest_day])
        elif self.succeeding_date:
            invalid = any([self.nth_day, self.preceding_date, self.nearest_day])

        if invalid:
            raise Exception(
                f"Cannot validate the Holiday. Please check the Holiday: {self.name}."
            )

    def get_nth_day_holiday(self, year: int) -> datetime.date:
        """
        Get holiday that has a rule of being nth day of a month.
        ex: Thanksgiving Day is 2nd Monday in October.
        """
        day_of_the_week_idx, n = get_day_of_the_week_idx(self.nth_day)
        day_in_first_week = cal.monthdatescalendar(year, self.month)[0][
            day_of_the_week_idx
        ]
        if day_in_first_week.month == self.month:
            return cal.monthdatescalendar(year, self.month)[n - 1][day_of_the_week_idx]
        else:
            return cal.monthdatescalendar(year, self.month)[n][day_of_the_week_idx]

    def get_preceding_day_holiday(self, year: int) -> datetime.date:
        """
        Get holiday that has a rule of being a day before a certain date
        ex: Victoria Day is Monday before May 25th.
        """
        day_of_the_week_idx, preceding_day = get_day_of_the_week_idx(
            self.preceding_date
        )
        precede_date = None

        if isinstance(preceding_day, str):
            order_of_day, day_str = parse_preceding_day_str(preceding_day)
            if order_of_day.lower() == "last":
                precede_date = get_last_day_str_of_month(
                    year, self.month, day_str.lower()
                )
            elif preceding_day == "Easter Sunday":
                precede_date = find_easter_day(year)
        else:
            precede_date = datetime.date(year, self.month, preceding_day)
        precede_day_idx = precede_date.weekday()
        delta_days = abs(precede_day_idx - day_of_the_week_idx)
        # Find 'day_str' before easter_day
        return precede_date - datetime.timedelta(days=delta_days)

    def get_succeeding_day_holiday(self, year: int) -> datetime.date:
        """
        Get holiday that has a rule of being a day after a certain date.
        ex: Easter Monday is a Monday after Easter Sunday.
        """
        day_of_the_week_idx, succeeding_day = get_day_of_the_week_idx(
            self.succeeding_date
        )

        if succeeding_day == "Easter Sunday":
            succeed_date = find_easter_day(year)
        else:
            succeed_date = datetime.date(year, self.month, succeeding_day)
        succeed_day_idx = succeed_date.weekday()
        delta_days = abs(succeed_day_idx - day_of_the_week_idx)
        return succeed_date + datetime.timedelta(days=(7 - delta_days))

    def get_nearest_day_holiday(self, year: int) -> datetime.date:
        """
        Get holiday that has a rule of being a day nearest to a certain date.
        ex: St. George's Day is a Monday that's nearest to April 23rd.

        Example of calculating a nearest Monday (0):
        - if the given, certain date is on 23rd:
            - if 23 is Tuesday (1)   Monday (0) day - delta:1
            - if 23 is Wednesday (2) Monday (0) day - delta:2
            - if 23 is Thursday (3)  Monday (0) day - delta:3
            - if 23 is Friday (4)    Monday (0) day + (7 - delta:4)
            - if 23 is Saturday (5)  Monday (0) day + (7 - delta:5)
            - if 23 is Sunday (6)    Monday (0) day + (7 - delta:6)
        """
        day_of_the_week_idx, _ = get_day_of_the_week_idx(self.nearest_day)
        nearest_date = datetime.date(year, self.month, self.nearest_day[1])
        nearest_day_str_idx = nearest_date.weekday()
        delta_days = abs(day_of_the_week_idx - nearest_day_str_idx)

        if delta_days < 4:
            return nearest_date - datetime.timedelta(delta_days)
        else:
            return nearest_date + datetime.timedelta(7 - delta_days)

    def to_date(self, year: int):
        """
        Calculate the datetime.date of the given holiday.
        """
        if self.month and self.day:
            return datetime.date(year, self.month, self.day)

        date = None
        if self.nth_day:
            date = self.get_nth_day_holiday(year)
        elif self.preceding_date:
            date = self.get_preceding_day_holiday(year)
        elif self.succeeding_date:
            date = self.get_succeeding_day_holiday(year)
        elif self.nearest_day:
            date = self.get_nearest_day_holiday(year)

        return date
