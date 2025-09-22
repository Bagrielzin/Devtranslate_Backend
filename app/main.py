# app/main.py
from dotenv import load_dotenv
load_dotenv()

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

origins = [
    "http://localhost:5173",  # Para desenvolvimento local (ajuste a porta se necessário)
    "https://seu-frontend.vercel.app" # URL que a Vercel vai te dar
]

app = FastAPI(title="DevTranslate API")

# CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(translate.router)