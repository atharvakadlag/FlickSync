from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import user as user_model  # Import your User model
from ..database import get_db  # Import your database connection function
from ..utils import hash_password  # Import your password hashing function

router = APIRouter()


@router.post("/users/", response_model=user_model.User)
def create_user(user: user_model.UserCreate, db: Session = Depends(get_db)):
    # Check if the username or email is already taken
    existing_user = db.query(user_model.User).filter(
        (user_model.User.username == user.username) | (user_model.User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    # Hash the password and create the user
    hashed_password = hash_password(user.password)
    db_user = user_model.User(**user.model_dump(), hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=user_model.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=user_model.User)
def update_user(user_id: int, user_update: user_model.UserUpdate, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}", response_model=user_model.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user
