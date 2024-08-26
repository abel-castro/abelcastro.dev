from datetime import datetime, timedelta
from typing import Optional

from django.utils import timezone


def get_date_30_days_ago() -> Optional[datetime]:
    return (timezone.now() - timedelta(days=30)).date()
