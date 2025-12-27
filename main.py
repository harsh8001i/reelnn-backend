
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from auth import login, verify_token
from telegram_stream import stream_video, download_video, list_subtitles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login_route(data: dict):
    return login(data)

@app.get("/stream/{id}")
async def stream(id: int, user=Depends(verify_token)):
    return await stream_video(id)

@app.get("/download/{id}")
async def download(id: int, user=Depends(verify_token)):
    return await download_video(id)

@app.get("/subtitles/{id}")
async def subtitles(id: int, user=Depends(verify_token)):
    return await list_subtitles(id)

@app.get("/health")
def health():
    return {"status": "ok"}
