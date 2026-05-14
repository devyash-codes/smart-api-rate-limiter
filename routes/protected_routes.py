from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from db.dependencies import get_db
from utils.dependencies import get_api_key
from services.request_log_service import log_request

from utils.rate_limiter import check_rate_limit

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@router.get("/protected_route")
def protected_route(
    request: Request,
    api_key = Depends(get_api_key),
    db: Session = Depends(get_db)
):
    check_rate_limit(
    db=db,
    api_key_id=api_key.id
)

    log_request(
        db=db,
        api_key_id=api_key.id,
        endpoint=request.url.path,
        status_code=200
    )

    return {
        "message": "Access granted",
        "owner_id": api_key.owner_id
    }
