from app import models, risk_justification
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine



app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, tags=['RiskJustifications'], prefix="/api/risk_justifications")


@app.get("/api/healthchecker")
def root():
    return {"message": "Healthly"}