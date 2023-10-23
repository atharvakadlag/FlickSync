from fastapi import FastAPI

app = FastAPI()

# Include your user routes
from .routes import user_routes  # noqa: E402
from .routes import movie_routes  # noqa: E402


app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(movie_routes.router, prefix="/movies", tags=["movies"])


@app.get("/")
def read_root():
    return {"message": "Hello, FlickSync!"}
