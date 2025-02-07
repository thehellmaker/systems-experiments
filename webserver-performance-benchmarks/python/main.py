from typing import Union

from fastapi import FastAPI

app = FastAPI()


from pydantic import BaseModel


class Item(BaseModel):
    graphName: str


@app.post("/test")
def read_root(item: Item):
    print(item.graphName)
    return item
