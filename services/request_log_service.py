from sqlalchemy.orm import Session

from models import RequestLog


def log_request(
    db: Session,
    api_key_id: int,
    endpoint: str,
    status_code: int
):

    log = RequestLog(
        api_key_id=api_key_id,
        endpoint=endpoint,
        status_code=status_code
    )

    db.add(log)
    db.commit()

    return log