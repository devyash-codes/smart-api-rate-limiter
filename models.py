from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql import func 
from sqlalchemy.types import DateTime, Float

from sqlalchemy.orm import relationship

from db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    username = Column(String, unique=True, index=True)
    
    email = Column(String, unique=True, index=True)
    
    api_keys = relationship("APIKey", back_populates="owner")

class APIKey(Base):
    __tablename__ = 'api_keys'

    id = Column(Integer, primary_key=True, index=True)

    key = Column(String, unique=True, index=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), default=func.now())

    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="api_keys")

    request_log = relationship("RequestLog", back_populates="api_key")

class RequestLog(Base):
    __tablename__ = 'request_logs'

    id = Column(Integer, primary_key=True, index=True)

    method = Column(String)

    status_code = Column(Integer)

    api_key_id = Column(Integer, ForeignKey('api_keys.id'))

    timestamp = Column(DateTime(timezone=True), default=func.now())

    endpoint = Column(String)

    response_time = Column(Float)

    api_key = relationship("APIKey", back_populates="request_log")




