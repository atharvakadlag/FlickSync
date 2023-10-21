from contextlib import contextmanager
from sqlmodel import create_engine
from sqlmodel import Session as SQLModelSession

# Define the SQLite database URL (in-memory or file-based)
DATABASE_URL = "sqlite:///dev.db"  # For a file-based database named dev.db

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)


@contextmanager
def Session():
    session = SQLModelSession(engine)
    try:
        yield session
    finally:
        session.close()
