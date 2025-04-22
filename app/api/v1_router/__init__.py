from fastapi import APIRouter
from . import user_router, project_router, team_router, auth_router, notification_router, file_router

router = APIRouter()
# Include all routers
router.include_router(user_router.router, prefix="/user", tags=["User"])
router.include_router(project_router.router, prefix="/project", tags=["Project"])
router.include_router(team_router.router, prefix="/team", tags=["Team"])
router.include_router(auth_router.router, prefix="/auth", tags=["AUTH"])
router.include_router(notification_router.router, prefix="/notification", tags=["Notification"])
router.include_router(file_router.router, prefix="/file", tags=["File"])