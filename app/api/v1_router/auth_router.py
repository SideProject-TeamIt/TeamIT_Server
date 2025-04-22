from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Auth"])
async def auth_ping():
    return {"ping": "pong!"}