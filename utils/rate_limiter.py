from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import RequestLog


RATE_LIMIT = 5


def check_rate_limit(
    db: Session,
    api_key_id: int
):

    one_minute_ago = datetime.now(timezone.utc) - timedelta(minutes=1)

    request_count = (
        db.query(RequestLog)
        .filter(
            RequestLog.api_key_id == api_key_id,
            RequestLog.timestamp >= one_minute_ago
        )
        .count()
    )

    if request_count >= RATE_LIMIT:

        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )