from fastapi import APIRouter

router = APIRouter(
    prefix="/inference",
    tags=["Inferências"]
)


@router.get("/")
async def inference():
    return {"inference": "Hello World!"}
