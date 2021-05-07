from fastapi import FastAPI, Request
from fastapi import APIRouter
from typing import Optional
router = APIRouter()
from api.models.predict import predict_image_from_url

@router.get("/predict/")
async def read_item(request: Request,img:str):
    results = predict_image_from_url(img)
    return results