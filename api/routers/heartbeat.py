
from fastapi import APIRouter

from api.models.heartbeat import HearbeatResult
from fastapi import FastAPI, Request

router = APIRouter()

@router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
async def get_hearbeat(request: Request, id: str) -> HearbeatResult:
    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat
