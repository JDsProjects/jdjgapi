import asyncio
import json
import random
from io import BytesIO

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from gtts import gTTS

data = json.loads("jdjg_data.json")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to jdjg api"}


@app.get("/api/")
async def api():
    return {"endpoints": "wip"}


@app.get("/api/objection")
async def objection():
    text = data["objection"]

    return {"url": random.choice(text)}

    # not sure how to return it


@app.get("/api/advice/")
async def advice():
    text = data["objection"]

    return {"text": random.choice(text)}


@app.get("/api/noslur/")
async def noslur():
    text = data["noslur"]

    {"text": random.choice(text)}


@app.get("/api/random-message/")
async def random_message():
    text = data["randomMessage"]

    return {"text": random.choice(text)}


@app.get("/api/insult/")
async def insult():
    text = data["insult"]

    return {"text": random.choice(text)}


@app.get("/api/compliment/")
async def compliment():
    text = data["compliment"]

    return {"text": random.choice(text)}


@app.get("/api/opinional/")
async def opinional():
    text = data["opinional"]

    return {"url": random.choice(text)}


@app.get("/api/tts")
async def tts(text: str, language: str):
    # calls tts

    languages = await asyncio.to_thread(gtts.lang.tts_langs)

    if language not in languages:
        raise HTTPException(status_code=404, detail="language not found")

    mp3_fp = BytesIO()
    data = await asyncio.to_thread(gTTS, text)
    data_write = asyncio.to_thread(tts.write_to_fp, mp3_fp)

    return FileResponse(data, media_type="audio/mpeg", filename="audio.mp3")


# handle 404 errors.
# return HTTPException
# raise HTTPException(status_code=404, detail="Item not found")


app.run(host="0.0.0.0", port=3000)
