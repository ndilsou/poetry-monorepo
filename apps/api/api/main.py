from typing import Union

from core.logging import get_logger
from core import do_core_stuff
from fastapi import FastAPI

logger = get_logger(__name__)


app = FastAPI()


@app.get("/")
def read_root():
    logger.info("hellow world sent")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    msg = do_core_stuff()
    return {"item_id": item_id, "q": q, msg: msg}
