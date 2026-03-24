from fastapi import FastAPI
from api.v1.router import proxy_router as proxy_api_router

app = FastAPI(title="proxy_service")
app.include_router(proxy_api_router, prefix="/api/v1")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
