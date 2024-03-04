import asyncio
import json
import random
import typing
from contextlib import asynccontextmanager
from io import BytesIO

import asqlite
import gtts
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from gtts import gTTS


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with asqlite.create_pool("bot.db") as app.pool:
        yield


app = FastAPI(lifespan=lifespan)


async def get_conn(request: Request):
    async with request.app.pool.acquire() as conn:
        yield conn


def get_particular_data(table):
    async def wrapper(conn=Depends(get_conn)):
        async with conn.cursor() as cursor:
            result = await cursor.execute(f"SELECT * FROM IMPORT {table}")
            return [x[0] for x in await result.fetchall()]

    return wrapper


@app.get("/")
async def root():
    return JSONResponse(content={"message": "welcome to jdjg api"})


@app.get("/api")
async def api():

    url_list = [route.name for route in app.routes if route.path.startswith("/api")]

    return JSONResponse(content={"endpoints": url_list})


# maybe I should make just remove /api for the stuff below???


@app.get("/api/objection")
async def objection(data: dict[str, typing.Any] = Depends(get_particular_data("objection"))):
    text = data["objection"]

    return JSONResponse(content={"url": random.choice(text)})

    # not sure how to return it


@app.get("/api/advice")
async def advice(data: dict[str, typing.Any] = Depends(get_particular_data("advice"))):
    text = data["advice"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/noslur")
async def noslur(data: dict[str, typing.Any] = Depends(get_particular_data("no_slur"))):
    text = data["noslur"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/random-message")
async def random_message(data: dict[str, typing.Any] = Depends(get_particular_data("random_message"))):
    text = data["randomMessage"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/insult")
async def insult(data: dict[str, typing.Any] = Depends(get_particular_data("insult"))):
    text = data["insult"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/compliment")
async def compliment(data: dict[str, typing.Any] = Depends(get_particular_data("compliment"))):
    text = data["compliment"]

    return JSONResponse(content={"text": random.choice(text)})


@app.get("/api/opinional")
async def opinional(data: dict[str, typing.Any] = Depends(get_particular_data("opinional"))):
    text = data["opinional"]

    return JSONResponse(content={"url": random.choice(text)})


@app.get("/api/tts")
async def tts(text: typing.Union[str, None] = None, language: typing.Union[str, None] = None):
    # calls tts

    languages = await asyncio.to_thread(gtts.lang.tts_langs)

    if language not in languages:
        raise HTTPException(status_code=404, detail="language not found")

    mp3_fp = BytesIO()
    data = await asyncio.to_thread(gTTS, text, "com", language)

    try:
        await asyncio.to_thread(data.write_to_fp, mp3_fp)

    except Exception as e:
        return JSONResponse(content={"error": "language not around"})

    return Response(mp3_fp.getvalue(), media_type="audio/mpeg")


# handle 404 errors.
# return HTTPException
# raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run("main:app", port=2343, log_level="debug")
