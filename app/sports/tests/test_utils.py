from datetime import date
from sports.utils import get_date_2_weeks_ago
from freezegun import freeze_time


@freeze_time("2024-03-30")
def test_get_date_2_weeks_ago():
    expected_date = date(2024, 3, 16)
    assert get_date_2_weeks_ago() == expected_date


I
