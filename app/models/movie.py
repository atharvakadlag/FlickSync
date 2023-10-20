from pydantic import BaseModel


class MovieBase(BaseModel):
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
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
