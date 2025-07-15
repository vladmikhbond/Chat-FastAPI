from .data import write_all, read_all, do_test_db
from .models import Item
from datetime import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

app = FastAPI()

# папки static і templates повинні знаходитися в кореневому каталозі пакета
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

do_test_db()


#####################################################

@app.get("/items")
async def get_items(request: Request):
    items = read_all()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@app.post("/items")
async def post_items(request: Request):
    form = await request.form()
    message = form.get("message")
    sign = form.get("sign")
    items = read_all()
    if message.strip() != "": 
        item = Item(message=message, sign=sign, datetime= datetime.now().isoformat())
        items.append(item)
        write_all(items)
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@app.get("/freq")
async def get_freq(request: Request):
    items = read_all()
    dict = {}
    for item in items:
        n: int = dict.get(item.sign, 0)
        dict[item.sign] = n + 1
    
    return templates.TemplateResponse("freq.html", {"request": request, "dict": dict})

