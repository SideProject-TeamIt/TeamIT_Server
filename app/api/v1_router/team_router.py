from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Team"])
async def team_ping():
    return {"ping": "pong!"}
