from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Comment"])
async def Comment_ping():
    return {"ping": "pong!"}