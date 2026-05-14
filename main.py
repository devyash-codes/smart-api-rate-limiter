from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.api_key_routes import router as api_key_router
from routes.protected_routes import router as protected_router
from routes.analytics_routes import router as analytics_router


app = FastAPI(
    title="Smart API Rate Limiter API",
    description="""
Production-style backend system featuring:

- API key authentication
- PostgreSQL persistence
- request analytics
- rate limiting
- Dockerized deployment
- usage tracking
    """,
    version="1.0.0"
)


app.include_router(user_router)
app.include_router(api_key_router)
app.include_router(protected_router)
app.include_router(analytics_router)

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from utils.exceptions import (
    http_exception_handler,
    validation_exception_handler
)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


@app.get("/")
def home():
    return {"Message": "Smart Rate Limiter API Backend"}



@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Smart API Rate Limiter Backend"
    }
