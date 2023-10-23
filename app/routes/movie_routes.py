from fastapi import APIRouter, Depends, HTTPException
from ..database import Session
from ..models import movie as movie_model

router = APIRouter()


@router.post("/movies/", response_model=movie_model.Movie)
def create_movie(movie: movie_model.MovieCreate, db: Session = Depends(Session)):
    with Session() as db:
        movie_data = movie.to_movie_model()
        db.add(movie_data)
        db.commit()
        db.refresh(movie_data)
        return movie_data


@router.get("/movies/{movie_id}", response_model=movie_model.Movie)
def read_movie(movie_id: int, db: Session = Depends(Session)):
    with Session() as db:
        movie = db.get(movie_model.Movie, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie


@router.put("/movies/{movie_id}", response_model=movie_model.Movie)
def update_movie(movie_id: int, movie_update: movie_model.MovieBase, db: Session = Depends(Session)):
    with Session() as db:
        movie = db.get(movie_model.Movie, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")

        for key, value in movie_update.dict(exclude_unset=True).items():
            setattr(movie, key, value)

        db.commit()
        db.refresh(movie)
        return movie


@router.delete("/movies/{movie_id}", response_model=movie_model.Movie)
def delete_movie(movie_id: int, db: Session = Depends(Session)):
    with Session() as db:
        movie = db.get(movie_model.Movie, movie_id)
        if movie is None:
            raise HTTPException(status_code=404, detail="Movie not found")
        db.delete(movie)
        db.commit()
        return movie
