from abc import ABC
from sqlalchemy import String,Integer,DateTime
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from datetime import datetime

class Base(DeclarativeBase):
    created_at=mapped_column(DateTime,default=datetime.utcnow)
    updated_at=mapped_column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class User(Base):
    __tablename__="users"

    id=mapped_column(Integer,primary_key=True, index=True)
    name=mapped_column(Integer,nullable=False, index=True)
    email=mapped_column(String(254), unique=True, nullable=False, index=True)
    mob=mapped_column(String(16), unique=True, nullable=False, index=True)
    password_hash=mapped_column(String(256), nullable=False, index=True)

    