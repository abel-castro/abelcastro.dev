from datetime import date
from sports.utils import get_date_30_days_ago
from freezegun import freeze_time


@freeze_time("2024-03-30")
def test_get_date_30_days_ago():
    expected_date = date(2024, 2, 29)
    assert get_date_30_days_ago() == expected_date
