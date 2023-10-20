from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str = None
    date_of_birth: str = None
    gender: str = None
    location: str = None
    bio: str = None
    profile_picture: str = None
    interests: list = []
    hashed_password: str = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
