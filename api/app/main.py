from typing import Optional

from fastapi import FastAPI

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = "what's this?"):
    breakpoint()
    return {"item_id": item_id, "q": q}


asyncio.run(serve(app, Config()))