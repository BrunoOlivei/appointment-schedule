import uvicorn
import json
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.core.config import get_config

config = get_config()

app = FastAPI(
    title=config.TITLE,
    openapi_url=f'{config.API_PREFIX_V1}/openapi.json'
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
    return Response(content=json.dumps({"message": "Hello World"}))


if __name__ == '__main__':
    uvicorn.run(app)
