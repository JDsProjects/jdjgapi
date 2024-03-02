from fastapi import FastAPI
import random
import json

data = json.loads(file.read())

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "welcome to jdjg api"}

@app.get("/api/")
async def api():
    return {"endpoints" : "wip"}

@app.get("/api/objection")
async def objection():
    text = data["objection"]

    return {"url" : random.choice(text)}

    # not sure how to return it

@app.get("/api/advice/")
async def advice():
    text = data["objection"]

    return {"text" : random.choice(text)}

@app.get("/api/noslur/")
async def noslur():
    text = data["noslur"]

    {"text" : random.choice(text)}

@app.get("/api/random-message/")
async def random_message():
    text = data["randomMessage"]

    return {"text" : random.choice(text)}

@app.get("/api/insult/")
async def insult():
    text = data["insult"]

    return {"text" : random.choice(text)}

@app.get("/api/compliment/")
async def compliment():
    text = data["compliment"]

    return {"text" : random.choice(text)}

@app.get("/api/opinional/")
async def opinional():
    text = data["opinional"]

    return {"url" : random.choice(text)}

# handle 404 errors.


app.run(host = '0.0.0.0', port=3000)

