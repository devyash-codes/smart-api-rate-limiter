from sqlalchemy.orm import Session
from models import APIKey
from utils.security import generate_api_key

def create_api_key(db: Session, user_id: int):

    new_key = APIKey(
        key=generate_api_key(),
        owner_id=user_id
    )

    db.add(new_key)
    db.commit()
    db.refresh(new_key)

    return new_key