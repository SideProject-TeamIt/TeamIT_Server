from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Comment"])
async def comment_ping():
    return {"ping": "pong!"}