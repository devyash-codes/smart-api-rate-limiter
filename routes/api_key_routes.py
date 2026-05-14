from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.dependencies import get_db
from services.api_key_service import create_api_key
from schemas import APIKeyResponse

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)

@router.post("/api_key/{user_id}", response_model=APIKeyResponse)
def generate_key(user_id: int, db: Session = Depends(get_db)):

    api_key = create_api_key(db, user_id)

    return api_key