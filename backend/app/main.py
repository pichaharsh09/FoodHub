import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .database.database import Base, engine
from . import models
from .exceptions import ResourceNotFoundError

from .routers import users, restaurants, foods, orders


Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    logger.info(
        "Request started: %s %s",
        request.method,
        request.url.path,
    )

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    logger.info(
        "Request completed: %s %s | Status: %s | Time: %.4fs",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    response.headers["X-Process-Time"] = str(round(process_time, 4))

    return response

# Global exception handler
@app.exception_handler(ResourceNotFoundError)
async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc) or "Resource not found"
        }
    )


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(users.router)
app.include_router(restaurants.router)
app.include_router(foods.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "Food Hub API is running"}
