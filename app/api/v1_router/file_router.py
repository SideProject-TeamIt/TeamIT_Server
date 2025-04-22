from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["File"])
async def file_ping():
    return {"ping": "pong!"}
