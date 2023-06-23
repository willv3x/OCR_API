from fastapi import FastAPI

from router import inference_router

api = FastAPI()

api.include_router(inference_router.router)

# uvicorn application:api
