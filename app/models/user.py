from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str
    email: str
    full_name: str = None
    date_of_birth: str = None
    gender: str = None
    profile_picture: str = None


class UserCreate(UserBase):
    password: str

    def to_user_model(self):
        # Create a User model from the DTO
        return User(
            username=self.username,
            email=self.email,
            full_name=self.full_name,
            date_of_birth=self.date_of_birth,
            gender=self.gender,
            profile_picture=self.profile_picture
        )


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = None

    class Config:
        from_attributes = True
