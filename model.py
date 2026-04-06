import datetime


class Calendar:
    REGIONAL_HOLIDAYS = {
        "obidos": ("01-11", "Reconquista Day"),
        "santarem": ("03-19", "Saint Joseph"),
        "arouca": ("05-02", "Queen Saint Mafalda"),
        "aveiro": ("05-12", "Saint Joana"),
        "caldas-da-rainha": ("05-15", "City Founding Day"),
        "leiria": ("05-22", "City and Diocese Day"),
        "lisbon": ("06-13", "Saint Anthony"),
        "cascais": ("06-13", "Saint Anthony"),
        "vila-real": ("06-13", "Saint Anthony"),
        "porto": ("06-24", "Saint John"),
        "braga": ("06-24", "Saint John"),
        "guimaraes": ("06-24", "Saint John"),
        "vila-nova-de-gaia": ("06-24", "Saint John"),
        "almada": ("06-24", "Saint John"),
        "sintra": ("06-29", "Saint Peter"),
        "evora": ("06-29", "Saint Peter"),
        "coimbra": ("07-04", "Queen Saint Isabel"),
        "viana-do-castelo": ("08-20", "Our Lady of Agony"),
        "funchal": ("08-21", "City Day"),
        "braganca": ("08-22", "Our Lady of Gracas"),
        "faro": ("09-07", "City Day"),
        "setubal": ("09-15", "Bocage Day"),
        "viseu": ("09-21", "Saint Matthew"),
        "portimao": ("12-11", "City Day"),
    }

    def __init__(self, year, region=None):
        if year < 1900 or year > 2099:
            raise ValueError("The year should be between 1900 and 2099")
        if region is not None and region.lower() not in self.REGIONAL_HOLIDAYS:
            raise ValueError(
                f"Unknown region: {region!r}. Available: {', '.join(self.REGIONAL_HOLIDAYS)}"
            )
        self.year = year
        self.region = region.lower() if region else None
        self._fixed_dates = {
            "01-01": "New Year",
            "04-25": "Liberty Day",
            "05-01": "Labour Day",
            "06-10": "Day of Portugal",
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
    def from_today(cls, region=None):
        return cls(datetime.date.today().year, region=region)

    @staticmethod
    def to_date(date: str) -> datetime.date:
        """
        date: string in ISO 8601 format, YYYY-MM-DD
        """
        return datetime.date.fromisoformat(date)

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

    @property
    def regional_holiday(self) -> dict:
        if self.region is None:
            return {}
        date_str, name = self.REGIONAL_HOLIDAYS[self.region]
        return {self.to_date(f"{self.year}-{date_str}"): name}

    def _all_holidays(self) -> dict:
        result = {**self.fixed_holidays, **self.flexible_holidays, **self.regional_holiday}
        return result

    def public_holidays(self) -> dict:
        """
        Returns the dictionary of public holidays related to the specified year
        """
        return {self.format_date(key): value for key, value in sorted(self._all_holidays().items())}

    def real_holidays(self) -> int:
        """
        Returns the number of public holidays that are not the same as a normal weekend
        """
        return sum(not self.is_weekend(date) for date in self._all_holidays().keys())

    def __repr__(self) -> str:
        region_str = f" ({self.region.replace('-', ' ').title()})" if self.region else ""
        return f"<Portugal Holidays Calendar for {self.year}{region_str}>"
