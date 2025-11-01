from fastapi import FastAPI
from routes.default import router as default_route
from routes.dummy import dummy_router as dummy_route
from routes.users import user_router as user_route
from routes.inventory import inventory_router as inventory_route
from routes.auth.register import user_register_router as user_register_route



#End Points
from resources.api_paths import (
    TEST_END_POINT,
    DUMMY_END_POINT,
    USER_END_POINT,
    INVENTORY_END_POINT,
    USER_REGISTER_END_POINT
)

def create_app() -> FastAPI:
    app = FastAPI(title="fastapi-app", version="1.0.0.0")
    app.include_router(default_route, prefix=TEST_END_POINT)
    app.include_router(dummy_route, prefix=DUMMY_END_POINT)
    app.include_router(user_route, prefix=USER_END_POINT)
    app.include_router(inventory_route, prefix=INVENTORY_END_POINT)
    app.include_router(user_register_route, prefix=USER_REGISTER_END_POINT)
    @app.get("/", include_in_schema=False)
    async def root_redirect():
        return {"docs": "/docs", "openapi": "/openapi.json"}
    return app

app = create_app()