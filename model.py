import datetime


class Calendar:
    def __init__(self, year):
        if year < 1900 or year > 2099:
            raise ValueError("The year should be between 1900 and 2099")
        self.year = year
        self._fixed_dates = {
            "01-01": "New Year",
            "04-25": "Liberty Day",
            "05-01": "Labour Day",
            "06-10": "Day of Portugal",
            "06-24": "Saint John Porto",
            "08-15": "Lady Day",
            "10-05": "Republic Implementation",
            "11-01": "All Saints Day",
            "12-01": "Independence Day",
            "12-08": "Immaculate Conception Day",
            "12-25": "Christmas",
        }
        self._relative_dates = {
            -47: "Carnival",
            -2: "Holy Friday",
            +0: "Easter",
            +60: "Body of Christ",
        }

    @classmethod
    def from_today(cls):
        return cls(datetime.date.today().year)

    @staticmethod
    def to_date(date: str) -> datetime.date:
        """
        date: string in ISO 8601 format, YYYY-MM-DD
        """
        try:
            return datetime.date.fromisoformat(date)
        except ValueError as exc:
            raise ValueError("The year should be 4-digit value") from None

    @staticmethod
    def is_weekend(date: datetime.date) -> bool:
        return date.isoweekday() > 5

    @staticmethod
    def format_date(date: datetime.date) -> str:
        return date.strftime("%d %b - %A")

    def easter(self) -> str:
        """
        An algorithm to find the date of Easter which is valid from 1900 to 2099
        Has been derived by Carter as follows
        """
        D = 225 - 11 * (self.year % 19)  # 19 = length of metonic cycle
        while D > 50:
            D -= 30
        if D > 48:
            D -= 1
        E = (self.year + self.year // 4 + D + 1) % 7
        Q = D + 7 - E
        # format Q to represent answer
        march_length = 31
        day = Q % march_length if Q > march_length else Q
        month = 3 + Q // (1 + march_length)
        return "-".join(["0" * (x < 10) + str(x) for x in [self.year, month, day]])

    @property
    def flexible_holidays(self) -> dict:
        return {
            self.to_date(self.easter()) + datetime.timedelta(days=key): value
            for key, value in self._relative_dates.items()
        }

    @property
    def fixed_holidays(self) -> dict:
        return {
            self.to_date("-".join([str(self.year), key])): value
            for key, value in self._fixed_dates.items()
        }

    def public_holidays(self) -> dict:
        """
        Returns the dictionary of public holidays related to the specified year
        """
        fix_dict = self.fixed_holidays
        flex_dict = self.flexible_holidays
        fix_dict.update(flex_dict)
        return {self.format_date(key): value for key, value in sorted(fix_dict.items())}

    def real_holidays(self) -> int:
        """
        Returns the number of public holidays that are not the same as a normal weekend
        """
        fix_dict = self.fixed_holidays
        flex_dict = self.flexible_holidays
        fix_dict.update(flex_dict)
        return sum(not self.is_weekend(date) for date in fix_dict.keys())

    def __repr__(self) -> str:
        return f"<Portugal Holidays Calendar for {self.year}>"
