import azure.functions as func
from .http_asgi import AsgiMiddleware
import fastapi
import random
import logging 
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from api.routers.router import api_router

def get_app() -> FastAPI:
    
    fast_app = FastAPI(title="Batman", version="1.0", debug=False)
    fast_app.include_router(api_router, prefix="/api/v{}".format(1))


    return fast_app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    app = get_app()
    return AsgiMiddleware(app).handle(req, context)