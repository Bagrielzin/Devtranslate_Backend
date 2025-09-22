# app/main.py
from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

app = FastAPI(title="DevTranslate API")

# Middleware de CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção pode restringir: ["https://meu-front.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(translate.router)

# Execução local (Railway ignora se usar Procfile/start command)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Railway fornece PORT
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
