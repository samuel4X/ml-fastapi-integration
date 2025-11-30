from fastapi import FastAPI
from app.routers.prediction import predict_router

app = FastAPI()

app.include_router(predict_router) 