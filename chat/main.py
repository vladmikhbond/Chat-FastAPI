from .data_file import read_all_items, add_item, do_test_db
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

#################### налаштування ###################

app = FastAPI()

# папки static і templates повинні знаходитися в кореневому каталозі пакета
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)


do_test_db()


#################### маршрути #########################

@app.get("/items")
async def get_items(request: Request):
    items = read_all_items()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@app.post("/items")
async def post_items(request: Request):
    form = await request.form()
    message = form.get("message")
    sign = form.get("sign")

    items = add_item(message, sign)
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@app.get("/freq")
async def get_freq(request: Request):
    items = read_all_items()
    dict = {}
    for item in items:
        n: int = dict.get(item.sign, 0)
        dict[item.sign] = n + 1
    
    return templates.TemplateResponse("freq.html", {"request": request, "dict": dict})

