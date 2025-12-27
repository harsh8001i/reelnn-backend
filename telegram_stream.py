
from pyrogram import Client
import os, tempfile
from fastapi.responses import StreamingResponse

client = Client(
    "reelnn",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

async def stream_video(msg_id):
    async with client:
        msg = await client.get_messages(os.getenv("CHANNEL_ID"), msg_id)
        return {"file_id": msg.video.file_id, "name": msg.video.file_name}

async def download_video(msg_id):
    async with client:
        msg = await client.get_messages(os.getenv("CHANNEL_ID"), msg_id)
        tmp = tempfile.NamedTemporaryFile(delete=False)
        await client.download_media(msg.video, tmp.name)
        return StreamingResponse(open(tmp.name,"rb"), media_type="video/mp4")

async def list_subtitles(movie_id):
    return [{"lang": "en", "label": "English"}]
