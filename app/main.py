from fastapi import FastAPI

app = FastAPI()

# Include your user routes
from .routes import user_routes  # Import your user routes  # noqa: E402


app.include_router(user_routes.router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Hello, FlickSync!"}
