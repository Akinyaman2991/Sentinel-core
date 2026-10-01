from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import engine
from app.models.event import Base

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    # Veritabanı tablolarını otomatik oluştur (Dev/Demo ortamı için)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "app": settings.PROJECT_NAME}