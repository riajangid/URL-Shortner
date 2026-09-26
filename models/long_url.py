from abc import ABC
from sqlalchemy import String,Integer,DateTime
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped 
from datetime import datetime
from models.user import Base

class Long_URL(Base):
    __tablename__="long_urls"
    long_url_id=mapped_column(Integer,primary_key=True, index=True) 
    user_id=mapped_column(Integer,unique=True, index=True) 
    long_url=mapped_column(String(256),nullable=False) 
    custom_alias=mapped_column(String(256),nullable=False) 
    expiry=mapped_column(DateTime(256),nullable=False) 