from fastapi import FastAPI

from database import engine
from models.user import Base

from routes.auth_router import router as auth_router
from routes.url_router import router as url_router
from routes.redirect_router import router as redirect_router

Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="URL Shortener"
)

app.include_router(auth_router)
app.include_router(url_router)
app.include_router(redirect_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )