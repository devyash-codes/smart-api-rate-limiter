from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import SessionLocal
from schemas import UserCreate, UserResponse
from services.user_service import (
    create_user,
    get_user_by_email
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# DB Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/create_user", response_model=UserResponse)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return create_user(
        db=db,
        name=user.name,
        email=user.email
    )