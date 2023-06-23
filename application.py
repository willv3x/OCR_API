from fastapi import FastAPI

from router import inference_router

application = FastAPI()

application.include_router(inference_router.router)

# uvicorn application:application
