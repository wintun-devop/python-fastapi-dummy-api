from fastapi import FastAPI
from .api.default import router as default_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(default_router, prefix="/user")
    return app

app = create_app()
