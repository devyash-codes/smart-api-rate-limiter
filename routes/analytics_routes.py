from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.dependencies import get_db
from models import RequestLog

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):

    total_requests = db.query(RequestLog).count()

    status_summary = (
        db.query(
            RequestLog.status_code,
            func.count(RequestLog.id)
        )
        .group_by(RequestLog.status_code)
        .all()
    )

    return {
        "total_requests": total_requests,
        "status_summary": status_summary
    }