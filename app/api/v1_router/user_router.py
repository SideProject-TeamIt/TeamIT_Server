from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["User"])
async def user_ping():
    return {"ping": "pong!"}
