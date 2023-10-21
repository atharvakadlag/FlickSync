from typing import Optional, List, AnyStr

from sqlmodel import Field, Session, SQLModel, create_engine


class Interest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    genre: str


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
            profile_picture=self.profile_picture,
            interests=self.interests,
        )


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = None


engine = create_engine("sqlite:///dev.db")


SQLModel.metadata.create_all(engine)

user_instance = User(
    username="johndoe",
    email="johndoe@example.com",
    full_name="John Doe",
    date_of_birth="1990-01-01",
    gender="Male",
    profile_picture="https://example.com/johndoe.jpg",
    # interests=["Reading", "Traveling", "Cooking"],
    hashed_password="hashed_password_here"
)


with Session(engine) as session:
    session.add(user_instance)
    session.commit()
