from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
import mimesis
from typing import Optional
router = APIRouter()
app = FastAPI()

app.mount("/static", StaticFiles(directory="api/static"), name="static")

templates = Jinja2Templates(directory="api/templates")

@router.get("/user/{user_id}")
async def read_item(request: Request, user_id: int, locale: Optional[str] = None):
    fake_user = mimesis.Person(locale=locale)
    data =  {
        "user_id": user_id,
        "username": fake_user.username(),
        "fullname": fake_user.full_name(),
        "age": fake_user.age(),
        "firstname": fake_user.first_name(),
        "lastname": fake_user.last_name(),
    }
    return data