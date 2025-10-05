from fastapi import FastAPI
from routes.default import router as default_route

#
from resources.api_paths import TEST_END_POINT

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(default_route, prefix=TEST_END_POINT)
    return app

app = create_app()