from fastapi import FastAPI
from routes.default import router as default_route


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(default_route, prefix="/user")
    return app

app = create_app()