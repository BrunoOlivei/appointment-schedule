import uvicorn
import json
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.core import router
from app.core.settings.config import get_config

config = get_config()

app = FastAPI(
    title=config.TITLE,
    description=config.DESCRIPTION,
    version=config.VERSION,
    openapi_url=f'{config.API_PREFIX_V1}{config.OPENAPI_URL}',
    docs_url=f'{config.API_PREFIX_V1}{config.DOCS_URL}',
    redoc_url=f'{config.API_PREFIX_V1}{config.REDOC_URL}',
    openapi_prefix=config.OPENAPI_PREFIX,
    debug=config.DEBUG,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "OK"}


@app.get("/openapi.json")
async def get_openapi():
    return Response(
        json.dumps(app.openapi()),
        media_type="application/json",
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000, log_level="info", reload=True
    )
