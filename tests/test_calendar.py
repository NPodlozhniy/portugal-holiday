import pytest
import datetime
from model import Calendar


def test_easter():
    expected_dates = [
        "2018-04-01",
        "2019-04-21",
        "2020-04-12",
        "2021-04-04",
        "2022-04-17",
        "2023-04-09",
        "2024-03-31",
        "2025-04-20",
        "2026-04-05",
        "2027-03-28",
        "2028-04-16",
    ]
    calculated_dates = []
    for year in range(2018, 2029, 1):
        calculated_dates.append(Calendar(year).easter())
    assert expected_dates == calculated_dates


def test_public_holidays():
    expected_dict = {
        "01 Jan - Saturday": "New Year",
        "01 Mar - Tuesday": "Carnival",
        "15 Apr - Friday": "Holy Friday",
        "17 Apr - Sunday": "Easter",
        "25 Apr - Monday": "Liberty Day",
        "01 May - Sunday": "Labour Day",
        "10 Jun - Friday": "Day of Portugal",
        "16 Jun - Thursday": "Body of Christ",
        "24 Jun - Friday": "Saint John Porto",
        "15 Aug - Monday": "Lady Day",
        "05 Oct - Wednesday": "Republic Implementation",
        "01 Nov - Tuesday": "All Saints Day",
        "01 Dec - Thursday": "Independence Day",
        "08 Dec - Thursday": "Immaculate Conception Day",
        "25 Dec - Sunday": "Christmas",
    }
    assert expected_dict == Calendar(2022).public_holidays()


def test_real_holidays():
    expected_number = 11
    assert expected_number == Calendar(2022).real_holidays()


def test_from_today():
    calA = Calendar(datetime.date.today().year)
    calB = Calendar.from_today()
    assert isinstance(calB, Calendar)
    assert calA.public_holidays() == calB.public_holidays()
