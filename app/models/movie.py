from typing import Optional

from sqlmodel import Field, SQLModel


class MovieBase(SQLModel):
    title: str
    description: str
    genre: str
    release_year: int
    director: str
    cast: str
    runtime: int
    rating: float = None
    cover_image: str = None
    trailer_url: str = None


class MovieCreate(MovieBase):

    def to_movie_model(self):
        return Movie(**self.dict())


class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    class Config:
        from_attributes = True
