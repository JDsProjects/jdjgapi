import asyncio
import json
import random
from io import BytesIO

import gtts
import uvicorn
from fastapi import FastAPI, HTTPException, JSONResponse
from fastapi.responses import FileResponse
from gtts import gTTS

with open("jdjg_data.json", "r") as f:
    file = f.read()

data = json.loads(file)

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(content={"message": "welcome to jdjg api"})


@app.get("/api/")
async def api():

    url_list = [route.name for route in app.routes if route.path.startswith("/api")]

    return JSONResponse(content={"endpoints": url_list})

# maybe I should make just remove /api for the stuff below???

@app.get("/api/objection/")
async def objection():
    text = data["objection"]

    return JSONResponse(content={"url": random.choice(text)})

    # not sure how to return it


@app.get("/api/advice/")
async def advice():
    text = data["advice"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/noslur/")
async def noslur():
    text = data["noslur"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/random-message/")
async def random_message():
    text = data["randomMessage"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/insult/")
async def insult():
    text = data["insult"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/compliment/")
async def compliment():
    text = data["compliment"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/opinional/")
async def opinional():
    text = data["opinional"]

    return JSONResponse(content={"url": random.choice(text)})


@app.get("/api/tts/")
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

if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, log_level="debug")
