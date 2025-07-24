from fastapi import FastAPI
from v1.endpoints import api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(router=api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vite's default dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


