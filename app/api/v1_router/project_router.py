from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Project"])
async def project_ping():
    return {"ping": "pong!"}
