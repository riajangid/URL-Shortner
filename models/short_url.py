from abc import ABC
from sqlalchemy import String,Integer,DateTime
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from datetime import datetime
from models.user import Base

class Short_URL(Base):
    __tablename__="short_urls"
    short_url_id=mapped_column(Integer,primary_key=True, index=True)
    user_id=mapped_column(Integer,unique=True, index=True) 
    short_code=mapped_column(String(256),unique=True, index=True) 
    long_url_id=mapped_column(Integer,unique=True, index=True) 
    short_url=mapped_column(String(256),nullable=False)
