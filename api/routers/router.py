

from fastapi import APIRouter

from api.routers import heartbeat,home,user

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(home.router, tags=["home"], prefix="/home")
api_router.include_router(user.router, tags=["user"])
