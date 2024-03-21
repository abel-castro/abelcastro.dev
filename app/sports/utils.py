from datetime import datetime, timedelta
from django.utils import timezone
from typing import Optional


def get_date_30_days_ago() -> Optional[datetime]:
    return (timezone.now() - timedelta(days=30)).date()
