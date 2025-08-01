from fastapi import FastAPI
from routes.csv_routes import router as csv_router

app = FastAPI(
    title="CSV Data API",
    description="Exposes CSV data over RESTful endpoints",
    version="1.0.0"
)

app.include_router(csv_router, prefix="/api")
