from pydantic import BaseModel, EmailStr
from datetime import datetime

# USERS
class UserCreate(BaseModel):
    name : str
    email : EmailStr
    mob : str
    password : str

class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr

    model_config={
        "from_attributes":True
    }    

# AUTH
class LoginRequest(BaseModel):
    email : EmailStr
    password : str

class LoginResponse(BaseModel):
    access_token : str
    token_type : str    

# URLS
class URLCreate(BaseModel):
    long_url : str
    custom_alias : str | None
    expiry : datetime | None

class URLResponse(BaseModel):
    short_code : str
    short_url : str
    long_url : str

    model_config={
            "from_attributes":True
        }   