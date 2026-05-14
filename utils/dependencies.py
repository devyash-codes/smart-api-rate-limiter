from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from models import APIKey


def get_api_key(
    x_api_key: str = Header(...),
    db: Session = Depends(get_db)
):

    api_key = (
        db.query(APIKey)
        .filter(APIKey.key == x_api_key)
        .first()
    )

    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return api_key