from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Notification"])
async def notification_ping():
    return {"ping": "pong!"}
